from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import HomeForm, UniquecodeForm, EmailForm
from .models import Dlsnp
from django.core.files import File
from django.core.mail import send_mail

import os
from project4.settings import BASE_DIR
tmppath = os.path.join(BASE_DIR, 'media/tmp_dlsnp')

import tarfile
import zipfile

import subprocess

import DLSNPv1.globalvars as Globalvars

def homepage(request):
    
    form = HomeForm(request.POST, request.FILES or None)
    if request.method == 'POST':

       if form.is_valid():
          form.save()
          uniquecodeis = request.POST.get('unique_code')
          Globalvars.y = uniquecodeis
          uploadedgenomeobject = Dlsnp.objects.get(unique_code=uniquecodeis)
          request.session['uploadedgenomeid'] = uploadedgenomeobject.id
          
          # send unique code to user email 
          useremailis = request.POST.get('user_email')
          Globalvars.z = useremailis
          if useremailis != 'liulabdellserver@gmail.com':
          #request.session['useremailis'] = request.POST.get('user_email')
               send_mail('Your Unique Code', 'Your unique code is '+uniquecodeis, 'liulabdellserver@gmail.com', [useremailis], fail_silently=False)
          
          # take the value of genus_species
          #request.session['genusspecies'] = request.POST.get('genus_species')
          
          return redirect('annotation')
          #return HttpResponseRedirect('process/')
    return render(request, 'DLSNPv1/homepage.html', {'form': form})

def annotation(request):
    fileidis = request.session['uploadedgenomeid']
    print(fileidis)
    annotationobject = get_object_or_404(Dlsnp, pk=fileidis)
    makerunningfiles(fileidis, annotationobject.data_file)
    
    ###### the variable will be shared with websocket.py ########################################
    #Globalvars.x = fileidis
    Globalvars.x = '{}/{}/outlog.txt'.format(tmppath,fileidis)
    #print(Globalvars.x)
    #print("bash should run here")
    os.system('bash '+'{}/{}/bashbatch.sh >{}/{}/outlog.txt 2>&1 &'.format(tmppath,fileidis,tmppath,fileidis))

    return render(request, 'DLSNPv1/annotation.html')

def process(request):
    # storage the annotation results with .zip format into related database by model's method 
    fileidis = request.session['uploadedgenomeid']
    annotationobject = get_object_or_404(Dlsnp, pk=fileidis)
    filewithpath = '{}/AnnotateResults_{}.zip'.format(tmppath,fileidis)
    filenameonly = 'AnnotateResults_{}.zip'.format(fileidis)
    annotationobject.add_predict_result(filewithpath, filenameonly)
    
    #validate unique code of user and then download result
    yourcode = UniquecodeForm(request.POST or None)
    if request.method == 'POST':
       if yourcode.is_valid():
          uniquecodeis = request.POST.get('uniquecode')
          try:
              annotationfile = Dlsnp.objects.get(unique_code=uniquecodeis)
          except:
              return render(request, 'DLSNPv1/processpage.html',{'yourcode':yourcode, 'uniquecodeis':uniquecodeis})
          else:
              request.session['downloadfileid']=annotationfile.id
              return redirect('download')
    return render(request, 'DLSNPv1/processpage.html',{'yourcode':yourcode})

def download(request):
    fileidis = request.session['downloadfileid']
    #downloadedfile = Annotation.objects.get(pk=fileidis)
    downloadedobject = get_object_or_404(Dlsnp, pk=fileidis)
    return render(request, 'DLSNPv1/download.html', {'downloadedobject':downloadedobject})
    
def about(request):
    return render(request, 'DLSNPv1/about.html')
def contact(request):
    return render(request, 'DLSNPv1/contact.html')
def tutoral(request):
    return render(request, 'DLSNPv1/tutoral.html')


def email(request):
    # input email address
    youremail = EmailForm(request.POST or None)
    if request.method == 'POST':
       if youremail.is_valid():
          youremailis = request.POST.get('email')
          request.session['emailis'] = request.POST.get('email')
          send_mail('Your Unique Code', 'Here is email test.', 'liulabdellserver@gmail.com', [youremailis], fail_silently=False)
          #return redirect('download')
    return render(request, 'DLSNPv1/email.html',{'youremail':youremail})
###################### not view functions ################################
def makerunningfiles(fileid, file_for_annotation):
    fileidis = fileid
    if not os.path.exists('{}/{}'.format(tmppath,fileidis)):
        os.makedirs('{}/{}'.format(tmppath,fileidis))
    with open('{}/{}/sequence_for_annotation.txt'.format(tmppath,fileidis), 'wb+') as destination:
        for chunk in file_for_annotation.chunks():
            destination.write(chunk)
    with open('{}/{}/bashbatch.sh'.format(tmppath,fileidis), 'w+') as destination:
         destination.write("echo progress5\n")
         destination.write('export PATH="/home/ydong/Desktop/DL_prediction/bedtools2-2.30.0/bin:/home/ydong/Desktop/GAAP/Augustus/bin:/home/ydong/Desktop/GAAP/Augustus/scripts:/home/ydong/vapid/VAPiD-master:/home/ydong/vadr-dir/vadr:/home/ydong/ncbi-blast-2.10.1+-src/c++/ReleaseMT/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/ydong/.dotnet/tools:/opt/mssql-tools/bin:/home/ydong/prokka/bin:/home/ydong/Desktop/BEACON/BEACON_Source:/home/ydong:/home/ydong/TRF-master/build/src:/home/ydong/maker/bin:/home/ydong/RepeatMasker::/opt/mssql-tools/bin:/opt/mssql-tools/bin:/home/ydong/.local/bin:/home/ydong/GenemarkES/gmes_linux_64:$PATH"\n')
         destination.write("echo progress10\n")
         #destination.write('cp -r '+'{}/SNP_prediction'.format(tmppath)+' '+'{}/{}/\n'.format(tmppath,fileidis))
         #destination.write('cp -r '+'{}/genome'.format(tmppath)+' '+'{}/{}/\n'.format(tmppath,fileidis))
         #destination.write('cp -r '+'{}/TRAINED_model'.format(tmppath)+' '+'{}/{}/'.format(tmppath,fileidis))

         destination.write('\ncd /home/ydong/Web_test/project4/media/tmp_dlsnp/SNP_prediction')
         #destination.write('\ncd /home/ydong/Web_test/project4/media/tmp_dlsnp/{}/SNP_prediction'.format(fileidis))

         destination.write('\npython3 snpToTensor.DLpredict.py ../{}/sequence_for_annotation.txt ../genome/genome_information_pl9.0.bed ../genome/PlasmoDB-26_Pfalciparum3D7_Genome.fasta ../{}/prediction_result.txt'.format(fileidis,fileidis))
         
         #destination.write('\npython3 snpToTensor.DLpredict.py ../sequence_for_annotation.txt ../genome/genome_information_pl9.0.bed ../genome/PlasmoDB-26_Pfalciparum3D7_Genome.fasta prediction_result.txt')
         
         destination.write("\necho progress95")
         
         destination.write('\ncd /home/ydong/Web_test/project4/media/tmp_dlsnp/{}'.format(fileidis))
         destination.write('\nzip -r AnnotateResults_{}.zip * -x bashbatch.sh'.format(fileidis))
         destination.write('\nmv '+'{}/{}/AnnotateResults_{}.zip'.format(tmppath,fileidis,fileidis)+' '+'{}'.format(tmppath))       
         #destination.write('\ntar -czvf {}.tar.gz {} --exclude={}/bashbatch.sh'.format(fileidis,fileidis,fileidis))
         destination.write("\necho All annotations finish successfully!")
         destination.write("\necho progress100")
         
    

