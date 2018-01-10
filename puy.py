# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,re,ast,os,subprocess,requests,tempfile

cl = LINETCR.LINE()
cl.login(token='EoX1M6Q9ELUx6i3SIlJ0.v49TfwwrrE1egDz80w4QKa.gAbnyribSER3tdHYNNXOq45XJnPR/hm6Jd8i5ZkMjPw=')
cl.loginResult()
print "1\n"

ki = LINETCR.LINE()
ki.login(token="EoZYqW1A1rfWPFq9wtKd.NDTUuoFwHk9Lw62uGnNI3q.ZAQKmd/nDwfivdWo20WH9q5wa3G0OPlqzLXn7WQDojE=")
ki.loginResult()
print "2\n"

kk = LINETCR.LINE()
kk.login(token="EoDiHqEo5b6ktKhYAdk5.SzfTgudgfYCJ2Hp4sPMEvq.BGy4pdj/s2YO7Qb+w3vSRJJto+E44Vg5JEHv/dXe0kk=")
kk.loginResult()
print "3\n"

kc = LINETCR.LINE()
kc.login(token="Eo6cWNrfCq2jXBG8wC00.udjXm+oXWdAsPTVBgX3cWa.IUfJQU7HTif7fNZ0/2osc8IuBrJcVsYHkEwxH8SHs2c=")
kc.loginResult()
print "4\n"

kr = LINETCR.LINE()
kr.login(token="EoZa4tb0DwWBe00XcRvd.+EjGmcOL1XSCj/yTns2vBq.bp5KOCzHqf14LnDmgPHaiuDC9SAKdPwAErXOYpzec1E=")
kr.loginResult()
print "5\n"

ks = LINETCR.LINE()
ks.login(token="EohajOlw0272e3KdIRc3.UAcSMqonILLriuREirzzuW.BmROhh+wP+omKm3fBcAqsZqgaiUWYNcy1J09Ua9bnBU=")
ks.loginResult()
print "6\n"

kb = LINETCR.LINE()
kb.login(token="Eo2s0RJnn6jOTKGvovze.cizeQqNnfxR0s20S26siJG.bZtrSn5nRfKms9BiOZN9I9XFjYJftAtK38qCSc2fjXk=")
kb.loginResult()
print "7\n"

kj = LINETCR.LINE()
kj.login(token="Eooi3rqdAuWl3sInIl28./6IhiA909mDOlReutlH+Ea.EK6XGMwc62AHdU66IuYnLOrOa4IJXuoGy/AFFivUKss=")
kj.loginResult()
print "8\n"

print "=====[Sukses All Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')

botMessage ="""                 [*BotCommand*]

- Absen
- Respon
- Runtime
- Kezia1 copy @
- kezia2 copy @
- kezia3 copy @
- kezia4 copy @
- kezia5 copy @
- kezia6 copy @
- kezia7 copy @
- kezia8 copy @
- Setpoint on / Viewseen
- mention
- kez2:mention
- kez3:mention
- kez4:mention
- kez5:mention
- kez6:mention
- kez7:mention
- kez8:mention
- Backup all
- /bio
- kez1:bye
- kez2:bye
- kez3:bye
- kez4:bye
- kez5:bye
- kez6:bye
- kez7:bye
- kez8:bye
"""

mediaMessage ="""                 [*MediaCommand*]

- Gift
- Gift1 @
- Playstore (text)
- Fancytext: (text)
- /musik
- /lirik
- /ig
- Checkig (username)
- /apakah (text)
- /kapan (text)
- /hari (text)
- Youtubevideo: (text)
- Youtubesearch: (text)
- Image (text)
- Say-id (text)
- Say-en (text)
- Say-jp (text)
- Id@en
- Id@th"""

groupMessage ="""                 [*GroupCommand*]

- Invite creator
- Setpoint on
- Viewseen
- Mention
- Gn: (text)
- Recover
- Cancel
- Gcreator
- Gurl
- Ginfo
- List group
- Pict group: (groupname)
- Spam: (text)
- Kick: (mid)
- Invite: (mid)
- Invite
- Memlist
- Getgroup image
- Urlgroup image"""

setMessage ="""                 [*Kezia Settings*]

- kez:status
- kez:sambutan on
- kez:qr on
- kez:alwaysread on
- kez:sider on
- kez:kontak on
- kez:simsimi on
- kez:restart"""

creatorMessage ="""                 [*CreatorCommand*]

- Admin add @
- Admin remove @
- Crash
- /cnall
- /cn1
- /cn2
- /cn3
- /cn4
- /cn5
- /cn6
- /cn7
- /cn8
- Kickall
- Bc: (text)
- Nk: @
- Ulti @
- Join group: (groupname)
- Leave all group
- Leave group: (groupname)
- kez:tag on
- kez:restart
- Turn off"""

adminMessage ="""                 [*AdminCommand*]

- Admin
- All join / Sini
- kez2:join
- kez3:join
- kez4:join
- kez5:join
- kez6:join
- Ban @
- Unban @
- Clear ban
- Ban list
- Kill
- kick @
- Set member: 
- Ban group: 
- Del ban: 
- List ban
- Kill ban
- Glist
- Glistmid
- Cancel invite: (gid)
- Invitemeto: (gid)
- Acc invite
- Removechat
- kez:allprotect on/off
- kez:qr on/off
- kez:ghost on/off
- kez:autocancel on/off
- kez:invitepro on/off
- kez:join on/off
- kez:joincancelon/off
- kez:respon on/off
- kez:responkick on/off
- kez:leave on/off"""

helpMessage ="""                 [*H3LL0*]

- Help creator
- Help group
- Help admin
- Help bot
- Creator
- Admin
- Speed
- kez:status"""


KAC=[cl,ki,kk,kc,kr,ks,kb,kj]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kr.getProfile().mid
Emid = ks.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = kj.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid]
Creator=["uac8e3eaf1eb2a55770bf10c3b2357c33"]
admin=["uac8e3eaf1eb2a55770bf10c3b2357c33","u04420be1a19f11db8ef6a37a1520f426","u5a31c87ded167546e010a1b7edd36c72","u07457c501b91f911cb9fe553727dc78c","uc4f91334d9b4238ef79aa3f374bbf523","u95f5fcc0013c63589bd45685aeaeda24","ucd7959b8a4caebb8c6727d1e7faa3b40","u090199c43e846b7d519c93cd31ced228","u1c852b3e0cfc1fa5d0ee0df22aefd13f"]

contact = cl.getProfile()
backup1 = cl.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup2 = ki.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage                        
backup2.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup3 = kk.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage                        
backup3.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup4 = kc.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage                        
backup4.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup5 = kr.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage                        
backup5.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup6 = ks.getProfile()
backup6.displayName = contact.displayName
backup6.statusMessage = contact.statusMessage                        
backup6.pictureStatus = contact.pictureStatus

contact = kb.getProfile()
backup7 = kb.getProfile()
backup7.displayName = contact.displayName
backup7.statusMessage = contact.statusMessage                        
backup7.pictureStatus = contact.pictureStatus

contact = kj.getProfile()
backup8 = kj.getProfile()
backup8.displayName = contact.displayName
backup8.statusMessage = contact.statusMessage                        
backup8.pictureStatus = contact.pictureStatus

responsename = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName
responsename5 = kr.getProfile().displayName
responsename6 = ks.getProfile().displayName
responsename7 = kb.getProfile().displayName
responsename8 = kj.getProfile().displayName

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "AutoJoinCancel":True,
    "memberscancel":20,
    "Members":3,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':True,
    'Leave':True,    
    'detectMention':True,
    'kickMention':False,      
    'timeline':True,
    "Timeline":True,
    "comment1":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment2":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment3":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment4":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment5":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment6":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment7":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "comment8":"Hi Kezia here, AutoLike by Puy\n\nhttp://line.me/ti/p/~yapuy",
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":True,
    "Sambutan":False,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":True,    
    "Tag":True,
    "Sider":True,
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{},
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","^","???:","???:","???:","???:"]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        #if op.type == 5:
           #if wait["autoAdd"] == True:
        #      cl.findAndAddContactsByMid(op.param1)
        #      if(wait["message"]in[""," ","\n",None]):
        #        pass
        #      else:
        #        cl.sendText(op.param1,str(wait["message"]))

        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Hei" + ", " + nick[0] + "" + "\nJgn sider aja tuh gabung chat sini")
                                    else:
                                        cl.sendText(op.param1, "Hei" + ", " + nick[1] + "" + "\nBetah amat sider-_-")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
        
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = kk.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kk.sendText(op.param1, "Hei" + ", " + nick[0] + "" + "\nJgn sider aja tuh gabung chat sini")
                                    else:
                                        kk.sendText(op.param1, "Hei" + ", " + nick[1] + "" + "\nBetah amat sider-_-")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	              
	      

        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Amid:
		    ki.acceptGroupInvitation(op.param1)
 
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
		
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
		    
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)		    

            if op.param3 in Cmid:
		if op.param2 in Dmid:
		    kc.acceptGroupInvitation(op.param1)

            if op.param3 in Dmid:
		if op.param2 in Emid:
		    kr.acceptGroupInvitation(op.param1)

            if op.param3 in Emid:
		if op.param2 in Fmid:
		    ks.acceptGroupInvitation(op.param1)

            if op.param3 in Fmid:
		if op.param2 in Gmid:
		    kb.acceptGroupInvitation(op.param1)

            if op.param3 in Gmid:
		if op.param2 in Amid:
		    kj.acceptGroupInvitation(op.param1)
		    
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			Ti = cl.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass
                        
                        
                        
	    if op.type == 13:
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Hei " + cl.getContact(op.param2).displayName + "\nAnggota grup anda kurang dari 20 member\nIm sorry for that!")
                        cl.sendText(op.param1,"Owner https://line.me/ti/p/~yapuy")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
                            
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
                            
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                            
                            
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                            
                            
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True                        
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                            
                            
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                                                        
                            
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True                        
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kj.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                                                        
                            
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True                                                

        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hei " + cl.getContact(op.param2).displayName + "\nSelamat datang di " + str(ginfo.name) + ".")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
    
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"Selamat Jalan " + cl.getContact(op.param2).displayName +  ".")
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"

        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in Creator:
              if op.param2 in admin:
                  if op.param2 in Bots:
                      pass
                  else:
                      try:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          ki.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          ki.sendMessage(c)
                          ki.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True
                      except:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          ki.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          ki.sendMessage(c)
                          ki.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True


        if op.type == 26:
            msg = op.message



            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     ki.like(url[25:58], url[66:], likeType=1005)
                     kk.like(url[25:58], url[66:], likeType=1005)
                     kc.like(url[25:58], url[66:], likeType=1005)
                     kr.like(url[25:58], url[66:], likeType=1005)
                     ks.like(url[25:58], url[66:], likeType=1005)
                     kb.like(url[25:58], url[66:], likeType=1005)
                     kj.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     ki.comment(url[25:58], url[66:], wait["comment2"])
                     kk.comment(url[25:58], url[66:], wait["comment3"])
                     kc.comment(url[25:58], url[66:], wait["comment4"])
                     kr.comment(url[25:58], url[66:], wait["comment5"])
                     ks.comment(url[25:58], url[66:], wait["comment6"])
                     kb.comment(url[25:58], url[66:], wait["comment7"])
                     kj.comment(url[25:58], url[66:], wait["comment8"])
                     cl.sendText(msg.to,"Done Like")                     
                     wait['likeOn'] = False

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['.'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + ", Aku Bilang Jangan Ngetag Lagi " + cName + "\nJgn tag tag ampas!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Creator:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break                                
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break 
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + ", Dont Tag My Creator/Admin\nDia Lagi Sibuk",cName + ", Don't Tag My Creator/Admin\nHim busy fvck!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Creator:
                                  cl.sendText(msg.to,ret_)
                                  break                                
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break                                
                              
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            random.choice(KAC).sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            random.choice(KAC).sendText(msg.to,"Ditambahkan")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KAC).sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif cms(msg.text,["/creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uac8e3eaf1eb2a55770bf10c3b2357c33"}
                cl.sendMessage(msg)

            elif cms(msg.text,["Admin","admin"]):
              if admin == []:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uac8e3eaf1eb2a55770bf10c3b2357c33"}
                cl.sendMessage(msg)
              else:
                  mc = "????yin yang??*Admin Kezia*????yin yang??"
                  for mi_d in admin:
                      mc += "\n\n*> " +cl.getContact(mi_d).displayName + ""
                  cl.sendText(msg.to,mc + "")
                  print "[Command]Admin List executed"
 
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Sukses Menambahkan Admin Kezia")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Kezia Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["kez:adminlist","admin list","List admin"]:
              if admin == []:
                  cl.sendText(msg.to,"The Admin List Is Empty")
              else:
                  mc = "+-------------------------\n¦Admin Kezia\n¦-------------------------\n"
                  for mi_d in admin:
                      mc += "¦••> " +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc + "+-------------------------")
                  print "[Command]Admin List executed"
                 

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     groups = ki.getGroup(msg.to)      
                     groups = kk.getGroup(msg.to)                     
                     groups = kr.getGroup(msg.to)                     
                     groups = ks.getGroup(msg.to)                     
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 ki.findAndAddContactsByMid(target)     
                                 kk.findAndAddContactsByMid(target)  
                                 kr.findAndAddContactsByMid(target)  
                                 ks.findAndAddContactsByMid(target)  
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Limit Invite om")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                cl.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                cl.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                cl.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                cl.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                cl.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                cl.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                cl.sendText(msg.to,adminMessage)                
                

 
            elif msg.text in ["List group"]:
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "??%s?\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Access Denied For You im Sorry")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, " Denied For You im Sorry")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
                            h = ki.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Access Denied For You im Sorry")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Kezia disuruh keluar :(")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
		            kk.leaveGroup(i)
			    kc.leaveGroup(i)			    
		            kr.leaveGroup(i)
			    ks.leaveGroup(i)			    			    
			    cl.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")
 
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        cl.leaveGroup(i)
			ki.leaveGroup(i)
		        kk.leaveGroup(i)
			kc.leaveGroup(i)	
		        kr.leaveGroup(i)
			ks.leaveGroup(i)			
		    cl.sendText(msg.to,"Success Leave All Group")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    cl.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Sudah Aktif")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","kez:join on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["Join off","kez:join off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")
		    
		    
            elif msg.text in ["kez:joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"Auto JoinCancel Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez:joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")		    
		    
 
            elif msg.text in ["kez:respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez:respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")	
		    
		    
 
            elif msg.text in ["kez:responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez:responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")			  
 
            elif msg.text in ["kez:leave on"]:
		if msg.from_ in admin:
                    wait["Leave"] = True
                    cl.sendText(msg.to,"Leave Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")
		    
 
	    elif msg.text in ["kez:autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")		

	    elif msg.text in ["kez:autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")	
		    

	    elif msg.text in ["kez:invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                cl.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")		

	    elif msg.text in ["kez:ivitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                cl.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")		    

	    elif "kez:qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")	    	

	    elif "kez:qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")	    	

            elif msg.text in ["kez:tag on"]:
		if msg.from_ in Creator:
                    wait["Tag"] = True
                    cl.sendText(msg.to,"Auto Tag Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez:tag off"]:
		if msg.from_ in Creator:
                    wait["Tag"] = False
                    cl.sendText(msg.to,"Auto Tag Sudah Di Nonaktifkan")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")
                        

	    elif "kez:autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     cl.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        cl.sendText(msg.to,"Access Denied For You im Sorry")	     

	    elif "kez:autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     cl.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        cl.sendText(msg.to,"Access Denied For You im Sorry")	     

	    elif "kez:ghost on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = True
		     cl.sendText(msg.to,"Ghost Sudah Aktif")
	     else:
	        cl.sendText(msg.to,"Access Denied For You im Sorry")		     

	    elif "kez:ghost off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = False
		     cl.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
	     else:
	         cl.sendText(msg.to,"Access Denied For You im Sorry")		     

            elif msg.text in ["kez:allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True                     
                    cl.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez:allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False                    
                    cl.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")


            elif msg.text in ["kez:kontak on","Contact on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["kez:kontak off","Contact off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["kez:alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["kez:alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                

            elif msg.text in ["kez:sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Aktifkan?(*´?`*)?")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On?(´?`)/")

            elif msg.text in ["kez:sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Nonaktifkan( ^?^)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off(p'?`?)")
                        
                        
            elif "kez:sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"CekSider Aktif")
                
            elif "kez:sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Not set")                
                    
            elif "ngelina:sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                kk.sendText(msg.to,"CekSider Aktif")
                
            elif "ngelina:sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    kk.sendText(msg.to, "Cek Sider Off")
                else:
                    kk.sendText(msg.to, "Not set")                                             


            elif msg.text in ["kez:status"]:
                md = ""
		if wait["Sambutan"] == True: md+="¦??? Sambutan : On\n"
		else:md+="*Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="¦??? Auto Join : On\n"
                else: md +="*Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="¦??? Auto Join Cancel : On\n"
                else: md +="*Auto Join Cancel : Off\n"                
		if wait["Leave"] == True: md+="¦??? Leave : On\n"
                else: md +="*Leave : Off\n"                
		if wait["Contact"] == True: md+="¦??? Info Contact : On\n"
		else: md+="*Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="¦??? Auto Cancel : On\n"
                else: md+= "*Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="¦??? Invite Protect : On\n"
                else: md+= "*Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="*Qr Protect : On\n"
		else:md+="*Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="*Auto Kick : On\n"
		else:md+="*Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="*Ghost : On\n"
		else:md+="*Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="*Always Read : On\n"
		else:md+="*Always Read: Off\n"
		if wait["detectMention"] == True: md+="*Auto Respon : On\n"
		else:md+="*Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="*Auto Respon Kick : On\n"
		else:md+="*Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="*Auto Sider : On\n"
		else:md+="*Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="*Simisimi : On\n"
		else:md+="*Simisimi: Off\n"		
		if wait["Tag"] == True: md+="*Auto Tag : On\n"
		else:md+="*Auto Tag : Off\n"
                cl.sendText(msg.to,"+-------------------------\n""[*Kezia Status*]\n""-------------------------\n"+md+"+-------------------------\n")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " pls cek u gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif msg.text in ["Tagall","mention"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["kez4:mention"]:
                  group = kc.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      kc.sendMessage(msg)
                  except Exception as error:
                      print error                      

            elif msg.text in ["kez2:mention"]:
                  group = ki.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ki.sendMessage(msg)
                  except Exception as error:
                      print error

            elif msg.text in ["kez3:mention"]:
                  group = kk.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      kk.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["kez5:mention"]:
                  group = kr.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      kr.sendMessage(msg)
                  except Exception as error:
                      print error                      

            elif msg.text in ["kez6:mention"]:
                  group = ks.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ks.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["kez7:mention"]:
                  group = kb.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      kb.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["kez8:mention"]:
                  group = kj.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      kj.sendMessage(msg)
                  except Exception as error:
                      print error                      
                      
            elif msg.text in ["Setview","Setpoint on"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint Checked")
                print "Setview"

            elif msg.text in ["Viewseen"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "=READ LIST=\n 􀰂􀇉slap􏿿"
                        grp = '\n 􀰂􀇉slap􏿿 '.join(str(f) for f in dataResult)
                        total = '\n\n*Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + ""
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        cl.sendText(msg.to, "Auto Checkpoint")                        
                    else:
                        cl.sendText(msg.to, "Belum Ada Viewers")
                    print "Viewseen"
                    
	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["like post"]:
              if msg.from_ in admin:	    
                wait["likeOn"] = True
                cl.sendText(msg.to,"Shere Post nya yang mau di like")                

            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                cl.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                cl.sendText(msg.to,"Send Contact") 
                

	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                kk.findAndAddContactsByMid(midd)
                kc.findAndAddContactsByMid(midd)
                kr.findAndAddContactsByMid(midd)
                ks.findAndAddContactsByMid(midd)
                kb.findAndAddContactsByMid(midd)
                kj.findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,""+bc+"")
		    cl.sendText(msg.to,"Success.")
		else:
		    cl.sendText(msg.to,"Access Denied For You")

            elif msg.text in ["kez:cancel"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["kez2:cancel"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                ki.sendText(msg.to,"All invitations have been refused")
                
            elif msg.text in ["kez3:cancel"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                kk.sendText(msg.to,"All invitations have been refused")     
                
            elif msg.text in ["kez4:cancel"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                kc.sendText(msg.to,"All invitations have been refused")                                
                
            elif msg.text in ["kez5:cancel"]:
                gid = kr.getGroupIdsInvited()
                for i in gid:
                    kr.rejectGroupInvitation(i)
                kr.sendText(msg.to,"All invitations have been refused")                                
                
            elif msg.text in ["kez6:cancel"]:
                gid = ks.getGroupIdsInvited()
                for i in gid:
                    ks.rejectGroupInvitation(i)
                ks.sendText(msg.to,"All invitations have been refused")                                                

            elif msg.text in ["kez7:cancel"]:
                gid = kb.getGroupIdsInvited()
                for i in gid:
                    kb.rejectGroupInvitation(i)
                kb.sendText(msg.to,"All invitations have been refused")                                

            elif msg.text in ["kez8:cancel"]:
                gid = kj.getGroupIdsInvited()
                for i in gid:
                    kj.rejectGroupInvitation(i)
                kj.sendText(msg.to,"All invitations have been refused")                                

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["All join","Sini"]:
		if msg.from_ in admin:
		    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = kj.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kj.updateGroup(G)
                    kj.sendText(msg.to,"Please type 'help' for show the command.")
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez2:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")

            elif msg.text in ["kez3:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        
		    
            elif msg.text in ["kez4:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kc.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        		    
		    
            elif msg.text in ["kez5:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kr.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        		    
		    
            elif msg.text in ["kez6:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ks.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ks.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        		    
		    
            elif msg.text in ["kez7:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kb.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kb.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        		    

            elif msg.text in ["kez8:join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kj.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kb.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kj.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Access Denied For You im Sorry")        	
		    
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["kez2:bye"]:
              if wait["Leave"] == True:		    
                    ki.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                  
              
            elif msg.text in ["kez3:bye"]:
              if wait["Leave"] == True:		    
                    kk.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")    
		          
            elif msg.text in ["kez4:bye"]:
              if wait["Leave"] == True:		    
                    kc.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                                 		          
		          
            elif msg.text in ["kez5:bye"]:
              if wait["Leave"] == True:		    
                    kr.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                                 		          
		          
            elif msg.text in ["kez6:bye"]:
              if wait["Leave"] == True:		    
                    ks.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                                 		          		          
		          
            elif msg.text in ["kez7:bye"]:
              if wait["Leave"] == True:		    
                    kb.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                                 		          		          

            elif msg.text in ["kez8:bye"]:
              if wait["Leave"] == True:		    
                    kj.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                                 		          		          
		          
            elif msg.text in ["bye all","kez:pulang"]:
              if wait["Leave"] == True:
                    cl.sendText(msg.to,"Jahat :(")
                    kj.leaveGroup(msg.to)
                    kb.leaveGroup(msg.to)
                    ks.leaveGroup(msg.to)
                    kr.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    cl.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"Autoleave nya nonaktif")                    

            elif msg.text in ["byenointi"]:
              if wait["Leave"] == True:    
                    kj.sendText(msg.to,"Jahat :(")
                    cl.sendText(msg.to,"bodoamat")
                    kj.leaveGroup(msg.to)
                    kb.leaveGroup(msg.to)
                    ks.leaveGroup(msg.to)
                    kr.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    ki.leaveGroup(msg.to)
              else:
		          kj.sendText(msg.to,"Autoleave nya nonaktif")                    
		          
            elif msg.text in ["kez:bye","@Bye"]:
              if wait["Leave"] == True:	
		    cl.leaveGroup(msg.to)
		    wait["Leave"] = False
              else:
		          cl.sendText(msg.to,"Access Denied For You im Sorry")		     
		    

            elif msg.text in ["Absen"]:
		cl.sendText(msg.to,"Keziaaaaaaaa hereeeeeeee")
                ki.sendText(msg.to,"Keziaaaaaaaa hereeeeeee")
                kk.sendText(msg.to,"Keziaaaaaaaa hereeeeee")
                kc.sendText(msg.to,"Keziaaaaaaaa hereeeee")
                kr.sendText(msg.to,"Keziaaaaaaaa hereeee")
                ks.sendText(msg.to,"Keziaaaaaaaa hereee")
                kb.sendText(msg.to,"Keziaaaaaaaa heree")
                kj.sendText(msg.to,"Keziaaaaaaaa here")

            elif msg.text.lower() in ["respon"]:
                cl.sendText(msg.to,responsename)
                ki.sendText(msg.to,responsename2)
                kk.sendText(msg.to,responsename3)
                kc.sendText(msg.to,responsename4)
                kr.sendText(msg.to,responsename5)
                ks.sendText(msg.to,responsename6)
                kb.sendText(msg.to,responsename7)
                kj.sendText(msg.to,responsename8)

            elif msg.text in ["Speed","Sp"]:
                start = time.time()
                cl.sendText(msg.to, "...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))


            elif "Nk: " in msg.text:
		if msg.from_ in Creator:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                ki.kickoutFromGroup(msg.to,[target])
                                ki.leaveGroup(msg.to)
                                ki.sendText(msg.to,"hehe")
			    else:
			        cl.sendText(msg.to,"Admin Detected")
		else:
		    cl.sendText(msg.to,"ngapain?")
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes BosQ")
                                except:
                                    cl.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KAC).sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes BosQ")
                            except:
                                cl.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"Cleared Banlist") 

            elif msg.text.lower() in ["bot","Kezia"]:
                cl.sendText(msg.to,"Knp kak?Kezia disini,\nKetik Help Untuk Bantuan") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist asw")
		else:
		    cl.sendText(msg.to, "Access Denied For You im Sorry")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = ki.getGroup(msg.to)
                        ki.sendText(msg.to,"Sampai jumpaa~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[ki]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","kez:restart"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Kezia berhasil di reboot.")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "Access Denied For You im Sorry")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                cl.sendMessage(msg)

 
            elif "kezia copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e

            elif "kezia2 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia2 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
                                
            elif "kezia3 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia3 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kk.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kk.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kk.CloneContactProfile(target)
                               kk.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                
                                
            elif "kezia4 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia4 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kc.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kc.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kc.CloneContactProfile(target)
                               kc.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                                                
                                
            elif "kezia5 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia5 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kr.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kr.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kr.CloneContactProfile(target)
                               kr.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                                                
                                
            elif "kezia6 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia6 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ks.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ks.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ks.CloneContactProfile(target)
                               ks.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                                                                                

            elif "kezia7 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia7 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kb.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kb.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kb.CloneContactProfile(target)
                               kb.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                                                                                

            elif "kezia8 copy @" in msg.text:
              if msg.from_ in Creator:
                   _name = msg.text.replace("kezia8 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kj.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kj.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kj.CloneContactProfile(target)
                               kj.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e                                                                                                

            elif msg.text in ["Backup all"]:
                try:
                    kj.updateDisplayPicture(backup8.pictureStatus)
                    kj.updateProfile(backup8)                                      
                    kb.updateDisplayPicture(backup7.pictureStatus)
                    kb.updateProfile(backup7)                                      
                    ks.updateDisplayPicture(backup6.pictureStatus)
                    ks.updateProfile(backup6)                                      
                    kr.updateDisplayPicture(backup5.pictureStatus)
                    kr.updateProfile(backup5)                                      
                    kc.updateDisplayPicture(backup4.pictureStatus)
                    kc.updateProfile(backup4)                                      
                    kk.updateDisplayPicture(backup3.pictureStatus)
                    kk.updateProfile(backup3)                  
                    ki.updateDisplayPicture(backup2.pictureStatus)
                    ki.updateProfile(backup2)
                    cl.updateDisplayPicture(backup1.pictureStatus)
                    cl.updateProfile(backup1)
                    cl.sendText(msg.to, "Done Backup")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    
 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendAudioWithURL(msg.to,abc)
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						cl.sendText(msg.to, "Lagu " + song[0] + "\nProses...")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)

            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            #elif msg.text.lower() in ["pap owner","pap creator"]:
                                #link = ["http://dl.profile.line-cdn.net/0hNPsZWL9WEX9OIz0lhyFuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03"]
                                #pilih = random.choice(link)
                                #cl.sendImageWithURL(msg.to,pilih)

 
           # elif "Spam: " in msg.text:
           #       bctxt = msg.text.replace("Spam: ", "")
           #       t = 10
           #       while(t):
           #         random.choice(KAC).sendText(msg.to, (bctxt))
           #         t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = cl.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      cl.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = cl.getAllContactIds()
                  for manusia in orang:
                    cl.sendText(manusia, (broadcasttxt))

 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kc.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kc.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

 
            elif "@Mkhadaffy." in msg.text:
              if wait["Tag"] == True:
                tanya = msg.text.lower().replace("@Mkhadaffy. ","")
                jawab = ("Berisik Jangan Tag Si Puy","Puy nya Lagi Off\nKalo penting pc aja puy nya")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    puy = "Hai juga ka " +cl.getContact(msg.from_).displayName + "."
                    cl.sendText(msg.to,puy)

            elif "playstore " in msg.text.lower():
                puy = msg.text.lower().replace("playstore ","")
                cl.sendText(msg.to,"Title : "+puy+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + puy)


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass


            elif "/allbio " in msg.text:
                    string = msg.text.replace("/allbio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        kr.updateProfile(profile)
                        ks.updateProfile(profile)
                        kb.updateProfile(profile)
                        kj.updateProfile(profile)
                        cl.sendText(msg.to,"All Done")
                        
            elif "/bio " in msg.text:
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")                        
                        
            elif "/bio2 " in msg.text:
                    string = msg.text.replace("/bio2 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki.getProfile()
                        profile.statusMessage = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Done")                                                
                        
            elif "/bio3 " in msg.text:
                    string = msg.text.replace("/bio3 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kk.getProfile()
                        profile.statusMessage = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"Done")                                                

            elif "/bio4 " in msg.text:
                    string = msg.text.replace("/bio4 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kc.getProfile()
                        profile.statusMessage = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Done")                        

            elif "/bio5 " in msg.text:
                    string = msg.text.replace("/bio5 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kr.getProfile()
                        profile.statusMessage = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Done")         
                        
            elif "/bio6 " in msg.text:
                    string = msg.text.replace("/bio6 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = ks.getProfile()
                        profile.statusMessage = string
                        ks.updateProfile(profile)
                        ks.sendText(msg.to,"Done")                        
                        
            elif "/bio7 " in msg.text:
                    string = msg.text.replace("/bio7 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kb.getProfile()
                        profile.statusMessage = string
                        kb.updateProfile(profile)
                        kb.sendText(msg.to,"Done")                        

            elif "/bio8 " in msg.text:
                    string = msg.text.replace("/bio8 ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kj.getProfile()
                        profile.statusMessage = string
                        kj.updateProfile(profile)
                        kj.sendText(msg.to,"Done")            
                        
            elif "/cnall" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnall")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile = ki.getProfile()
                        profile = kk.getProfile()
                        profile = kc.getProfile()
                        profile = kr.getProfile()
                        profile = ks.getProfile()
                        profile = kb.getProfile()
                        profile = kj.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        kr.updateProfile(profile)
                        ks.updateProfile(profile)
                        kb.updateProfile(profile)
                        kj.updateProfile(profile)
                        cl.sendText(msg.to,"Done")

            elif "/cn1" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn1")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
                        
            elif "/cn4" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn4")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Done")                        

            elif "/cn2" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn2")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Done")
                        
            elif "/cn3" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn3")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"Done")   
                        
            elif "/cn5" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn5")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kr.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Done")   
                        
            elif "/cn6" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn6")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ks.getProfile()
                        profile.displayName = string
                        ks.updateProfile(profile)
                        ks.sendText(msg.to,"Done")                           
                        
            elif "/cn7" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn7")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kb.getProfile()
                        profile.displayName = string
                        kb.updateProfile(profile)
                        kb.sendText(msg.to,"Done")                           

            elif "/cn8" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cn8")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kj.getProfile()
                        profile.displayName = string
                        kj.updateProfile(profile)
                        kj.sendText(msg.to,"Done")                           
                        
            elif "Ulti " in msg.text:
              if msg.from_ in Creator:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        ki.kickoutFromGroup(msg.to,[target])
                                        ki.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        ki.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)


            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["kez:simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                cl.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["kez:simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                cl.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="---------List Friend---------"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n---------List Friend---------\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="---------List Member-?????--------"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n---------List Member---------\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)

            

            elif msg.text in ["Spam"]:
#              if msg.from_ in admin:
                cl.sendText(msg.to,"aaaaaaaaaaaaaaaaaaaaaaaaaa")
                ki.sendText(msg.to,"bbbbbbbbbbbbbbbbbbbbbbb")
                kk.sendText(msg.to,"ccccccccccccccccccccccccccccccccccccc")
                kc.sendText(msg.to,"ddddddddddddddddddddddddddddddddd")
                kr.sendText(msg.to,"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                ks.sendText(msg.to,"fffffffffffffffffffffffffffffffffff")

            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "kez2:spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        ki.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "kez3:spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = kk.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        kk.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "kez4:spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = kc.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        kc.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "kez5:spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "kez6:spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = ks.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        ks.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kr.removeAllMessages(op.param2)
                        ks.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            ki.findAndAddContactsByMid(msg.from_)
                            kk.findAndAddContactsByMid(msg.from_)
                            kc.findAndAddContactsByMid(msg.from_)
                            kr.findAndAddContactsByMid(msg.from_)
                            ks.findAndAddContactsByMid(msg.from_)
                            random.choice(KAC).inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "¦?" + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"+-------------------------\n¦LIST GROUPS\n¦-------------------------\n" + h + "¦-------------------------" + "\n¦ Total Groups =" +" ["+str(len(gid))+"]\n+-------------------------")

            elif msg.text in ["Glistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="---------List GrupMid---------"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n---------List GrupMid---------\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.com/" + b)

            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    gid = ki.getGroup(gids)
                    gid = kk.getGroup(gids)
                    gid = kc.getGroup(gids)
                    gid = kr.getGroup(gids)
                    gid = ks.getGroup(gids)    
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                                ki.rejectGroupInvitation(i)
                                kk.rejectGroupInvitation(i) 
                                kc.rejectGroupInvitation(i) 
                                kr.rejectGroupInvitation(i) 
                                ks.rejectGroupInvitation(i) 
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    gid = ki.getGroupIdsInvited()
                    gid = kk.getGroupIdsInvited()
                    gid = kc.getGroupIdsInvited()
                    gid = kr.getGroupIdsInvited()
                    gid = ks.getGroupIdsInvited()
                    gid = kb.getGroupIdsInvited()
                    gid = kj.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            gids = ki.getGroup(i)
                            gids = kk.getGroup(i)
                            gids = kc.getGroup(i)
                            gids = kr.getGroup(i)
                            gids = ks.getGroup(i)
                            gids = kb.getGroup(i)
                            gids = kj.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                            ki.acceptGroupInvitation(i)
                            kk.acceptGroupInvitation(i)
                            kc.acceptGroupInvitation(i)
                            kr.acceptGroupInvitation(i)
                            ks.acceptGroupInvitation(i)
                            kb.acceptGroupInvitation(i)
                            kj.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")           

        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
