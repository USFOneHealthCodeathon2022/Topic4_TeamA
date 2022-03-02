
# ！/usr/bin/python3
# -*- coding: utf-8 -*-
import paramiko
import Ocean.globalvars as Globalvars
#import DLSNPv1.views

from django.core.mail import send_mail

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })

             # 这里根据web页面获取的值进行对应的操作
            if event['text'] == 'laying_eggs':
                print("Pipeline running")
                print(Globalvars.x)
                # 执行的命令或者脚本
                #command = 'bash /home/ydong/Web_test/test.sh'
                #logx = Globalvars.x.split("/")
                #logy = '/'.join(logx[:-1])
                #logz = logy + '/out.log 2>&1 &'
                searchstr = "progress"
                command = 'grep '+searchstr+' '+Globalvars.x
                # 远程连接服务器
                hostname = '10.119.34.34'
                username = 'ydong'
                password = 'yibo2020'

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostname, username=username, password=password)
                # 务必要加上get_pty=True,否则执行命令会没有权限
                stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
                # result = stdout.read()
                # 循环发送消息给前端页面
                
                ###################
                
                
                #######################
                while True:
                #xv = 0
                #while xv <10:
                    nextline = stdout.readline().strip()  # 读取脚本输出内容
                    # 发送消息到客户端
                    
                    if 'progress100' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': 'All annotations finish successfully'
                        })
                        if Globalvars.z != 'liulabdellserver@gmail.com': 
                           send_mail('Your Annotation Done', 'Your annotation at Integrative Genome Annotation Service has been completed!\nYour Unique Code: '+Globalvars.y+'\nYou can use the unique code to download the annotation result from the link http://10.119.34.34:8000/DLSNPv1/process.', 'liulabdellserver@gmail.com', [Globalvars.z], fail_silently=False)
                    elif 'progress95' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '95% annotation is complete'
                        })
                    elif 'progress90' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '90% annotation is complete'
                        })
                    elif 'progress60' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '60% annotation is complete'
                        })
                    elif 'progress30' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '30% annotation is complete'
                        })
                    elif 'progress10' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '10% annotation is complete'
                        })
                    elif 'progress5' in nextline:
                        await send({
                           'type': 'websocket.send',
                           'text': '5% annotation is complete'
                        })
                    else:
                        break
                    # 判断消息为空时,退出循环
                   # if not nextline:
                    #   break
                ssh.close()  # 关闭ssh连接
                # 关闭websocket连接
                await send({
                    'type': 'websocket.close',
                })
             #   if Globalvars.z != 'liulabdellserver@gmail.com': 
             #        send_mail('Your Annotation Done', 'Your annotation at Integrative Genome Annotation Service has been completed!\nYour Unique Code: '+Globalvars.y+'\nYou can use the unique code to download the annotation result from the link http://10.119.34.34:8000/GAv1/process.', 'liulabdellserver@gmail.com', [Globalvars.z], fail_silently=False)
