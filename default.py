### ############################################################################################################
###	#	
### # Site: 				#		
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re
try: import copy
except: pass
import urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui
import common as common
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath)
### ############################################################################################################
### ############################################################################################################
SiteName=ps('__plugin__')
SiteTag=ps('__plugin__').replace(' ','')
#mainSite=addst("site-domain")
#mainSite2='http://www.'+(mainSite.replace('http://',''))
mainSite="http://vaughnlive.tv"
mainSite2="https://vaughnlive.tv"
mainSite3="http://www.vaughnlive.tv"
mainSite4="https://www.vaughnlive.tv"
iconSite=_artIcon
fanartSite=_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan','13':'firebrick','14':'mediumpurple'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyGenres=['Action','Adventure','Animation','Comedy','Drama','Family','Fantasy','Thriller','Reality TV','Sport','Sci-Fi','Documentary','Mystery','Talk Show','War','History','Crime','Music','Horror']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
ww6='[COLOR black]@[/COLOR]'; 
ww7='[COLOR mediumpurple]@[/COLOR]'; 
colorA='FFFFFFFF'; colorB='FFAAAAAA'; colorC='FF777777'; 
workingUrl=mainSite+'ram.pls'
### ############################################################################################################
### ############################################################################################################
site=addpr('site',''); section=addpr('section',''); url=addpr('url',''); sections={'series':'series','movies':'movies'}; thumbnail=addpr('img',''); fanart=addpr('fanart',''); page=addpr('page',''); 
### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		m+='IRC Chat:  '+cFL('#TVADDONS','blueviolet')+' @ '+cFL('irc.Freenode.net','blueviolet')
		m+=CR+'Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		#m+=CR+CR+'Known Hosts for Videos:  '
		##m+=CR+'* TrollVid'
		##m+=CR+'* UploadCrazy'
		#m+=CR+CR+'Features:  '
		#m+=CR+'* Browse Shows'
		#m+=CR+'* Browse Episodes'
		#m+=CR+'* Browse Host Links'
		#m+=CR+'* Play Videos with UrlResolver'
		##m+=CR+'* Download Videos with UrlResolver'
		#m+=CR+'* Optional MetaData where available.'
		#m+=CR+'* MetaData for Shows and 1st Season Episodes where data is available.'
		#m+=CR+'* MetaData auto-disabled for Anime List - ALL.  This is to prevent hammering with the huge list of nearly 400 shows.'
		m+=CR+CR+'Notes:  '
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		m+=CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	import splash_highway as splash; splash.do_My_Splash(_addon.get_fanart(),5,False); 
	#splash.do_My_Splash(HowLong=5,resize=False); 
	#splash.do_My_Splash('http://i.imgur.com/tMKjZ6j.png',HowLong=5,resize=False); 
	
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()
def spAfterSplit(t,ss):
	if ss in t: t=t.split(ss)[1]
	return t
def spBeforeSplit(t,ss):
	if ss in t: t=t.split(ss)[0]
	return t
def AFColoring(t): 
	if len(t)==0: return t
	elif len(t)==1: return cFL(t,colorA) #colorA)
	else: return cFL(cFL_(t,colorA),colorB) #colorA),colorB)
def wwA(t,ww): #for Watched State Display
	if   ww==7: t=ww7+t
	elif ww==6: t=ww6+t
	return t

### ############################################################################################################
### ############################################################################################################
def psgn(x,t=".png"):
	s="http://i.imgur.com/"; d=iconSite #artp('default_icon')
	try:
		return {
			'popular': 				artp('browse_popular') #d #s+""+t
			,'entertainment': artp('browse_entertainment') #d #s+""+t
			,'gaming': 				artp('browse_gaming') #d #s+""+t
			,'music': 				artp('browse_music') #d #s+""+t
			,'social': 				artp('browse_social') #artp('default_user') #d #s+""+t
			,'history 101': 	artp('history_101')
			,'browse my picks list': 			artp('list_mypicks')
			,'browse local list': 				artp('list_local')
			,'browse devs featured': 			artp('featured_dev')
			,'browse featured': 					artp('featured_site')
			,'search': 										artp('search_channels') #s+"L8Ifj8L"+t #L8Ifj8L #MTnRQJ3
			,'search user': 							artp('search_people') #s+"L8Ifj8L"+t #MTnRQJ3
			,'img_next':									artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'img_prev':									artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			,'next':											artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'prev':											artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			,'browse':										d #artp('browse')
			,'topbar':										d #artp('browse')
			,'a': 		s+"OvFHLK2"+t
			,'b': 		s+"ezem9mn"+t
			,'c': 		s+"707ILz1"+t
			,'d': 		s+"BUT7dUz"+t
			,'e': 		s+"mzNtW2U"+t
			,'f': 		s+"11cykaC"+t
			,'g': 		s+"l0CvvHo"+t
			,'h': 		s+"VOupMGK"+t
			,'i': 		s+"ps3YPHq"+t
			,'j': 		s+"oNHwZWv"+t
			,'k': 		s+"TwHANG6"+t
			,'l': 		s+"xiuR2WX"+t
			,'m': 		s+"GDEAPud"+t
			,'n': 		s+"9FjSiMu"+t
			,'o': 		s+"TcR1pa0"+t
			,'p': 		s+"OGc4VBR"+t
			,'q': 		s+"hL9tEkx"+t
			,'r': 		s+"37NNHm8"+t
			,'s': 		s+"mFQswUE"+t
			,'t': 		s+"4DBQVrd"+t
			,'u': 		s+"qpovLUW"+t
			,'v': 		s+"bnu5ByY"+t
			,'w': 		s+"0IHoHV2"+t
			,'x': 		s+"ic81iKY"+t
			,'y': 		s+"46IlmRH"+t
			,'z': 		s+"PWUSCsE"+t
			,'0': 		s+"7an2n4W"+t # 0RJOmkw
			,'all': 	d #s+"hrWVT21"+t
			#,'search': 										s+"mDSHRJX"+t
			,'plugin settings': 					d #s+"K4OuZcD"+t
			,'local change log': 					d #s+"f1nvgAM"+t
			#,'last': 											s+"FelUdDz"+t
			#,'favorites': 								s+"lUAS5AU"+t
			#,'favorites 2': 							s+"EA49Lt3"+t
			#,'favorites 3': 							s+"lwJoUqT"+t
			#,'favorites 4': 							s+"Wr7GPTf"+t
			,'latest update': 						d #s+"dNCxQbg"+t
			,'completed': 								d #s+"xcqaTKI"+t
			#,'most popular': 							s+"T9LUsM2"+t
			#,'new anime': 								s+"BGZnMf5"+t
			#,'genre': 										s+"AmQHPvY"+t
			,'ongoing': 									d #s+"mBqFW3r"+t #EUak0Sg #ozEg86L
			,'anime list all': 						d #s+"t8b1hSX"+t
			,'anime list alphabet': 			d #s+"R0w0BAM"+t
			,'anime list latest update': 	d #s+"XG0LGQH"+t
			,'anime list newest': 				d #s+"eWAeuLG"+t
			,'anime list popularity': 		d #s+"eTrguP1"+t
			,'urlresolver settings': 			d #s+"PlROfSs"+t
			,'online bookmarks': 					d #s+"68ih1sx"+t
			#,'alphabetical': 							s+"sddCXQo"+t
			,'genre select': 							d #s+"MhNenb6"+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			,'about': 										s+"8BLYGft"+t
			,'alphabetical': 							d #s+"aLKvpQD"+t
			,'favorites': 								d #s+"mVxogXL"+t #
			,'favorites 1': 							d #s+"cyDyVuh"+t #
			,'favorites 2': 							d #s+"GxH6BbM"+t #yRtrel2
			,'favorites 3': 							d #s+"Z9zKGJU"+t #
			,'favorites 4': 							d #s+"ovjBVu3"+t #
			,'favorites 5': 							d #s+"n8LUh2R"+t #
			,'favorites 6': 							d #s+"qN6FEit"+t #
			,'favorites 7': 							d #s+"3yQYXNh"+t #
			,'genre': 										d #s+"ObKUcJT"+t #XEIr4Cz
			,'icon': 											d #s+"VshtskV"+t
			,'fanart': 										d #s+"OSv7S2u"+t
			,'last': 											d #s+"3g6S9UH"+t
			,'latest episodes': 					d #s+"Skoe3Fm"+t #r19ycox
			,'latest updates': 						d #s+"E86Rnq5"+t
			,'most popular': 							d #s+"DzFexnz"+t #N69lo3G
			,'new anime': 								d #s+"wZN1olE"+t
			,'random anime': 							d #s+"Rjag7b3"+t
			,'_': 												d #s+"bGMWifZ"+t
			,'anime 2013': 								d #s+"4SgqERs"+t
			,'anime 2014': 								d #s+"ijvRzvJ"+t
			,'anime 2015': 								d #s+"IYPai5I"+t
			,'anime 2016': 								d #s+"UqAYilt"+t
			,'anime list': 								d #s+"NTPFfwQ"+t
			,'a-z': 											d #s+"Br4ltnl"+t
			,'hot this season': 					d #s+"KcymQWL"+t
			,'latest animes': 						d #s+"mDFKTFN"+t
			,'movies': 										d #s+"hDYdtIr"+t
			,'random': 										d #s+"5uYkgTx"+t
			,'today': 										d #s+"GPxwlE8"+t
			,'tomorrow': 									d #s+"YX2EKk8"+t
			,'yesterday': 								d #s+"shqgyif"+t
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			###
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
# KissAnimeGenres
# http://imgur.com/a/rws19/all
# http://imgur.com/a/rws19#Q12cars
# http://imgur.com/a/rws19
		}[x.lower()]
	except: 
		print 'failed to find graphc for %s' % (x); 
		return d
		#return ''
### ############################################################################################################
### ############################################################################################################
def decrypt_vaughnlive(encrypted,retVal=""):
	for val in encrypted.split(':'): retVal+=chr(int(val.replace("0m0",""))/84/5)
	return retVal
def PlayLiveStream(pageUrl='',Name='',Thumb='',Channel='',roomId='',roomSlug='',plot='',liVe='',streamUrl='',streamkey='',youtubekey='',sourcetype='show'):
	PlayerMethod=addst("core-player"); url=''; print "--DO A PLAYER SPLIT HERE--"; debob(['pageUrl',pageUrl,'Name',Name,'Thumb',Thumb,'roomId',roomId,'roomSlug',roomSlug,'plot',plot,'liVe',liVe,'streamUrl',streamUrl]); fimg=''; 
	tempParams=_addon.queries; debob(['tempParams',tempParams]); 
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	if len(streamUrl) > 10: url=streamUrl
	else: 
		if pageUrl.startswith('/'): pageUrl=mainSite+pageUrl
		deb('pageUrl',pageUrl); 
		#if len(Channel) > 0: pageUrl=mainSite+"/embed/video/%s" % Channel
		if (len(pageUrl)==0) and (len(Channel) > 0): pageUrl=mainSite+"/%s" % Channel
		elif (not '://' in pageUrl): pageUrl=mainSite+pageUrl
		html=messupText(nolines(nURL(pageUrl)),True,True); deb('length of html',str(len(html))); #debob(html); 
		if len(Channel)==0:
			try:    Channel=re.compile('vsVars\d+.k2 = "(.+?)";').findall(html)[0]
			except: Channel=''
		#try: 		vidHash=re.compile("flashvars.roomId\s*=\s*'(.+?)';").findall(html)[0]
		#except: vidHash=''
		#try: 		SiteDomain=re.compile('://((?:[0-9A-Za-z]+\.)?[0-9A-Za-z]+\.[0-9A-Za-z]+)/";').findall(pageUrl)[0]; 
		#SD1='://((?:[0-9A-Za-z]+\.)?[0-9A-Za-z]+\.[0-9A-Za-z]+)/";'
		#SD1='://((?:www\.)?[0-9A-Za-z]+\.[0-9A-Za-z]+)/";'
		#SD1='//([0-9A-Za-z]+\.[0-9A-Za-z]+)/";'
		#try: 		SiteDomain=re.compile(SD1).findall(pageUrl)[0]; 
		try: 		SiteDomain=pageUrl.split('://')[1].split('/')[0]
		except: SiteDomain='vaughnlive.tv'
		debob(['SiteDomain',SiteDomain]); 
		try: 		liVe=re.compile('vsVars\d+.k1 = "(.+?)";').findall(html)[0]; 
		except: liVe=''
		debob(['liVe',liVe]); 
		try: 		TimeStampA=re.compile('vsVars\d+.t = "(\d+)";').findall(html)[0]; 
		except: TimeStampA=''
		debob(['TimeStampA',TimeStampA]); 
		try: 		vidServers=re.compile('(\d+\.\d+\.\d+\.\d+\:443)').findall(html); 
		except: vidServers=''
		debob(['vidServers',vidServers]); 
		try: 		vidServer=vidServers[0]; 
		except: vidServer=''
		if len(vidServer)==0: vidServer='live.%s:443' % SiteDomain; #'mvn.vaughnsoft.net:443/video/edge'
		#if len(vidServer)==0: vidServer='mvn.vaughnsoft.net/video/edge'
		debob(['vidServer',vidServer]); 
		##streamUrl="rtmp://%s/live?%s playpath=live_%s swfUrl=http://vaughnlive.tv/800021294/swf/VaughnSoftPlayer.swf live=1 pageUrl=http://vaughnlive.tv/embed/video/%s?viewers=true&watermark=left&autoplay=true Conn=S:OK --live" % (vidServer,vidHash,Channel,Channel); 
		#url="rtmp://%s/live? playpath=live_%s swfUrl=http://vaughnlive.tv/800021294/swf/VaughnSoftPlayer.swf live=1 pageUrl=http://vaughnlive.tv/embed/video/%s?viewers=true&watermark=left&autoplay=true Conn=S:OK --live" % (vidServer,Channel,Channel); 
		TOK=''; #TOK='token=30dabc4871922a1314192e925ab7961d'; 
		HaSH=''; #HaSH='lkS0dd2dfe8e8aeb3e9fa6d6999a4ddd921'; 
		try: 		HaSHa=re.compile('vsVars\d\d\d\d\d\d\d\d\d\d\d.[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]+\s+=\s+"(.+?)";').findall(html)[0]
		except: HaSHa=''
		try: 		HaSHb=re.compile(  'vsVars\d\d\d\d\d\d\d\d\d\d.[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]+\s+=\s+"(.+?)";').findall(html)[0]
		except: HaSHb=''
		try:		HaSHaa=decrypt_vaughnlive(HaSHa)
		except:	HaSHaa=''
		try:		HaSHbb=decrypt_vaughnlive(HaSHb)
		except:	HaSHbb=''
		debob(['HaSHa',HaSHa,HaSHaa]); debob(['HaSHb',HaSHb,HaSHbb]); 
		#HaSH=HaSHaa
		HaSH=HaSHbb
		LiveTag='live'
		if   'instagib.' in SiteDomain: LiveTag='instagib'
		elif 'vapers.'   in SiteDomain: LiveTag='vapers'
		elif 'breakers.' in SiteDomain: LiveTag='breakers'
		
		url="rtmp://%s/live?%s playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=1 timeout=30 pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SiteDomain,Channel,TOK); 
		#if   'vaughn'    in SiteDomain: url="rtmp://%s/live?%s playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=1 timeout=20 pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,Channel,SiteDomain,SiteDomain,TOK); 
		#el
		#if 'instagib.' in SiteDomain: url="rtmp://%s/live?%s playpath=%s_%s live=1 timeout=20" % (vidServer,HaSH,LiveTag,Channel); 
		#if 'instagib.' in SiteDomain: url="rtmp://%s/live?%s/%s_%s live=1 timeout=20" % (vidServer,HaSH,LiveTag,Channel); 
		#else: url="rtmp://%s/live?%s/%s_%s live=1 timeout=20" % (vidServer,HaSH,LiveTag,Channel); 
		
		#if len(Thumb)==0:
		#	try:    Thumb=re.compile("flashvars.roomAvatar\s*=\s*'(.+?)';").findall(html)[0]
		#	except: Thumb=iconSite
		Thumb=iconSite
		#if len(Name)==0:
		try:    Name=re.compile('<span id="videoTitle">(.+?)</span>').findall(html)[0]
		except: Name='Unknown'
		try: 		fimg='http://'+re.compile('div.theMain { background-image:url\(//(cdn.vaughnsoft.com/vaughnsoft/vaughnlive/background/[0-9A-Za-z]+_[0-9A-Za-z]+_[0-9A-Za-z]+.jpg)\);').findall(html)[0]
		except: fimg=fanartSite
		## ### ## 
		## ### ## 
	## ### ## 
	#try: _addon.resolve_url(url)
	#except: pass
	#try: play.play(url)
	#except: pass
	## ### ## 
	#pageUrl='',Name='',Thumb='',roomId='',roomSlug='',plot='',liVe='',streamUrl='',streamkey='',youtubekey='',sourcetype='show'
	debob(",['pars', {'streamurl': '%s', 'roomslug': '%s', 'fimg': '%s', 'img': '%s', 'title': '%s', 'url': '%s', 'type': '%s', 'live': '%s', 'mode': 'PlayStreamUP', 'roomid': '%s', 'sourcetype': '%s'}, " % (str(url),str(roomSlug),str(fimg),str(Thumb),str(Name).replace('[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR]',''),str(pageUrl),str(addpr('type','')),str(liVe),str(roomId),str(sourcetype))); 
	
	# return
	
	infoLabels={"Studio":liVe,"Title":'%s [%s]: %s' % (Channel,liVe,Name),"cover_url":Thumb,"background_url":fimg,'plot':plot}; 
	li=xbmcgui.ListItem(Name,iconImage=Thumb,thumbnailImage=Thumb); 
	li.setInfo(type="Video", infoLabels=infoLabels ); li.setProperty('IsPlayable', 'true'); 
	try: _addon.resolve_url(url)
	except: pass
	#pL=xbmc.PlayList; pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); pL.add(url,li); play.play(pL); 
	try: play.play(url,li,False,0)
	except:
		try: play.play(url)
		except: pass
	##logging().Logger().setLevel(30); 
	### ### ## 

def History101():
	tab1rows=ps('db channels tags0c'); 
	try:
		r=get_database_all('SELECT %s FROM channels' % (tab1rows)); 
	except: pass
	if r:
		if len(r) > 0:
			iC=len(r); i=0; 
			HistoryCountLimit="20"; #HistoryCountLimit=addst("history101-count"); 
			for k in r[::-1]:
				try:
					debob(['k',k]); 
					cMI=[]; pars={}; labs={}; pageurl=''; url=''; title=''; liVe=''; plot=''; streamtype=''; roomslug=''; roomid=''; img=iconSite; fanart=fanartSite; 
					try: pageurl=urllib.unquote_plus(str(k[0])); 
					except: pass
					try: title=urllib.unquote_plus(str(k[1])); 
					except: pass
					try: streamtype=urllib.unquote_plus(str(k[2])); 
					except: pass
					try: img=urllib.unquote_plus(str(k[4])); 
					except: pass
					try: fanart=urllib.unquote_plus(str(k[5])); 
					except: pass
					try: roomid=urllib.unquote_plus(str(k[6])); 
					except: pass
					try: roomslug=urllib.unquote_plus(str(k[7])); 
					except: pass
					try: url=urllib.unquote_plus(str(k[9])); debob(['url',url]); 
					except: pass
					try: labs[u'plot']=urllib.unquote_plus(str(k[17])); 
					except: labs[u'plot']=''
					labs[u'title']=cFL(title,colorA); 
					if (len(liVe) > 0) and (not str(liVe).lower()=='none'): labs[u'title']=cFL(title+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
					pars={'streamurl':str(url),'roomslug':str(roomslug),'fimg':str(fanart),'img':str(img),'title':str(title),'url':str(pageurl),'type':'','live':'History','mode':'PlayStreamUP','roomid':str(roomid),'sourcetype':''}; 
					if (len(url) > 0) and (not str(url).lower()=='none'):
						try: _addon.add_directory(pars,labs,is_folder=False,fanart=fanart,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False); i+=1; 
						except: pass
					if not (HistoryCountLimit=="ALL") and (len(HistoryCountLimit) > 0):
						if i > (int(HistoryCountLimit)-1): break
				except: pass
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()

def ListShows(Url,Page='',TyPE='js',idList='[]',csrfToken='',MeTHoD='re.compile'):
	#if len(csrfToken)==0: maipageHtml=nURL('http://vaughnlive.tv/',cookie_file=CookFile,load_cookie=False,save_cookie=True); tokenParam='content="(.*?)" name="csrf-token"'; csrfToken=re.compile(tokenParam).findall(maipageHtml)[0]; 
	## ### ## 
	debob(['Url',Url,'TyPE',TyPE])
	if len(Url)==0: debob("No url found."); return
	if (not mainSite in Url) and (not mainSite2 in Url) and (not mainSite3 in Url) and (not mainSite4 in Url): Url=mainSite+Url
	deb('Url',Url); 
	html=messupText(nolines(nURL(Url,headers={'Referer':mainSite})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: debob("No html found."); eod(); return
	## ### ## 
	if (mainSite+"/app/topbar.php?s=") in Url:
		s='<div\s+class="topbar_img">\s*<a\s+href="(\D+://(?:www.)?(?:/|vapers.tv/|breakers.tv/|vaughnlive.tv/|instagib.tv/)?)(.*?)"\s*>(())\s*<img\s+name="mvnPicTopBar_.*?"\s+width="\d*"\s+height="\d*" border="\d*"\s+onerror="mvnImages.profileError\(\'mvnPicTopBar_[0-9A-Za-z_\-]+\',\'[0-9A-Za-z_\-]+\'\);"\s+class="[0-9A-Za-z_\-]*"\s+alt="[0-9A-Za-z_\-]+(?: - \D+.)?"\s+title="[0-9A-Za-z_\-]+(?: - \D+.)?"\s*/>\s*</a>\s*</div'; 
		#MeTHoD='split'
	elif (mainSite+"/browse/") in Url:
		s='<a href="((?:http://)?(?:/|vapers.tv/|breakers.tv/|vaughnlive.tv/|instagib.tv/)?)(.+?)" target="_top"><img src="//(thumbnails.vaughnsoft.com/(\d+)/fetch/\D+/.+?.png)" class"browseThumb" width="\d*" height="\d*"\s*/></a>'; 
	else: return
	html=html.replace('</div>','</div\n\r\a>'); #debob(html); 
	if (MeTHoD=='split') and ('</MVN>' in html):
		debob(['MeTHoD',MeTHoD,'"</MVN>" is in HTML.']); 
		matches=html.split('</MVN>')[-1].split(',')
	elif (MeTHoD=='re.compile') or (not '</MVN>' in html): #MeTHoD=='re.compile':
		debob(['MeTHoD',MeTHoD,'"</MVN>" is not in HTML.']); 
		try: matches=re.compile(s).findall(html); deb('# of matches found',str(len(matches))); #debob(matches); 
		except: matches=''; debob('No matches were found.'); 
	else: matches=[]
	## ### ## 
	if len(matches) > 0:
		iC=len(matches); USER_AGENT='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0'; 
		if MeTHoD=='re.compile':
			for (PrefixD,match,img,iTS) in matches: #(img,url,name,genres)
				labs={}; cMI=[]; is_folder=False; plot=''; name=match.replace('_',' '); labs[u'plot']=plot; LocImgName=''; 
				img="http://cdn.vaughnsoft.com/vaughnsoft/vaughn/img_profiles/%s_125.jpg"%match
				fimg="http://cdn.vaughnsoft.com/vaughnsoft/vaughnlive/img_backgrounds/%s.jpg"%match #fimg=fanartSite; #deb('img',img); 
				if '://' in PrefixD:url=PrefixD+"%s" % match; urlPage=PrefixD+"%s" % match; urlEmbedVideo=PrefixD+"embed/video/%s" % match; urlEmbedChat=PrefixD+"embed/chat/%s" % match; 
				else: url=mainSite+"/%s" % match; urlPage=mainSite+"/%s" % match; urlEmbedVideo=mainSite+"/embed/video/%s" % match; urlEmbedChat=mainSite+"/embed/chat/%s" % match; 
				labs[u'title']=cFL(name,colorA); #labs[u'title']=cFL(name+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
				pars={'url':url,'title':name,'fimg':fimg,'img':img,'mode':'PlayLiveStream','channel':match,'site':site,'section':section,'sourcetype':'auto'}; 
				Clabs={'title':name,'year':'','url':url,'commonid':'','img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
				try: cMI=ContextMenu_LiveStreams(Clabs); 
				except: pass
				try: debob(['pars',pars,'labs',labs]); 
				except: pass
				cMI.append(('Visit Page', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlPage})))
				cMI.append(('Visit Video', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedVideo})))
				cMI.append(('Visit Chat', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedChat})))
				try: _addon.add_directory(pars,labs,is_folder=is_folder,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False)
				except: pass
		elif MeTHoD=='split':
			for (match) in matches: #(img,url,name,genres)
				if len(match.strip()) > 0:
					PrefixD=''; img=''; iTS=''
					labs={}; cMI=[]; is_folder=False; plot=''; name=match.replace('_',' '); labs[u'plot']=plot; LocImgName=''; 
					img="http://cdn.vaughnsoft.com/vaughnsoft/vaughn/img_profiles/%s_125.jpg"%match
					fimg="http://cdn.vaughnsoft.com/vaughnsoft/vaughnlive/img_backgrounds/%s.jpg"%match #fimg=fanartSite; #deb('img',img); 
					if '://' in PrefixD:url=PrefixD+"%s" % match; urlPage=PrefixD+"%s" % match; urlEmbedVideo=PrefixD+"embed/video/%s" % match; urlEmbedChat=PrefixD+"embed/chat/%s" % match; 
					else: url=mainSite+"/%s" % match; urlPage=mainSite+"/%s" % match; urlEmbedVideo=mainSite+"/embed/video/%s" % match; urlEmbedChat=mainSite+"/embed/chat/%s" % match; 
					labs[u'title']=cFL(name,colorA); #labs[u'title']=cFL(name+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
					pars={'url':url,'title':name,'fimg':fimg,'img':img,'mode':'PlayLiveStream','channel':match,'site':site,'section':section,'sourcetype':'auto'}; 
					Clabs={'title':name,'year':'','url':url,'commonid':'','img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
					try: cMI=ContextMenu_LiveStreams(Clabs); 
					except: pass
					try: debob(['pars',pars,'labs',labs]); 
					except: pass
					cMI.append(('Visit Page', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlPage})))
					cMI.append(('Visit Video', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedVideo})))
					cMI.append(('Visit Chat', 'XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedChat})))
					try: _addon.add_directory(pars,labs,is_folder=is_folder,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False)
					except: pass
	#		## ### ## 
	#		#if is_folder==False:
	#		#	sDB=[]; 
	#		#	#'pageurl, title, streamtype, live, thumb, fanart, roomid, roomslug, sourcetype, streamurl, streamkey, 
	#		#	#youtubeposition, youtubecurrentindex, youtubeduration, youtubeplaylistcount, youtubevideoid, youtubeuuid, 
	#		#	#plot, timestampyear, timestampmonth, timestampday'
	#		#	#'"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"'
	#		#	if url.startswith('/'): url=mainSite2+url
	#		#	GroupB=(  urllib.quote_plus(str(url)),urllib.quote_plus(str(name)),urllib.quote_plus(str(liVe)),urllib.quote_plus(str(img)),urllib.quote_plus(str(roomId)),urllib.quote_plus(str(roomSlug)),urllib.quote_plus(str(plot)),str(datetime.date.today().year),str(datetime.date.today().month),str(datetime.date.today().day)  )
	#		#	#sDB.append( 'INSERT OR REPLACE INTO channels ('+ps('db channels tags1a')+') VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % GroupB )
	#		#	sDB.append( 'INSERT INTO channels ('+ps('db channels tags1a')+') VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % GroupB )
	#		#	debob(sDB); 
	#		#	do_database(sDB); 
	#		#	#do_database_test(sDB); 
	#		## ### ## 
	#NextPage=str(int(page)+1); 
	#if (("page="+NextPage) in html) and (not TyPE=='js|featured'):
	#	_addon.add_directory({'mode':'ListShows','site':site,'url':Url,'page':NextPage,'type':str(TyPE),'idlist':str(ListOfIds),'csrfToken':csrfToken},{'title':cFL('>> Next %s' % cFL(NextPage,colorA),colorB)},is_folder=True,fanart=fanartSite,img=psgn('next'))
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()

def Fav_List(site='',section='',subfav=''):
	debob(['test1',site,section,subfav]); 
	favs=fav__COMMON__list_fetcher(site=site,section=section,subfav=subfav); 
	ItemCount=len(favs); 
	debob('test2 - '+str(ItemCount)); 
	if len(favs)==0: myNote('Favorites','None Found'); eod(); return
	debob(favs); 
	favs=sorted(favs,key=lambda item: (item[0],item[1]),reverse=False); 
	for (_name,_year,_img,_fanart,_Country,_Url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs:
		if _img > 0: img=_img
		else: img=iconSite
		if _fanart > 0: fimg=_fanart
		else: fimg=fanartSite
		debob('_ToDoParams'); debob(_ToDoParams)
		pars=_addon.parse_query(_ToDoParams)
		pars[u'fimg']=_fanart; pars[u'img']=_img; 
		#if len(_commonID) > 0: pars['imdb_id']=_commonID
		debob('pars'); debob(pars)
		_title=AFColoring(_name)
		if (len(_year) > 0) and (not _year=='0000'): _title+=cFL('  ('+cFL(_year,'mediumpurple')+')',colorA)
		if len(_Country) > 0: _title+=cFL('  ['+cFL(_Country,'mediumpurple')+']',colorA)
		wwT=_name+" ~~ "; 
		try:
			if visited_check2(wwT)==True: ww=7
			else: ww=6
		except: ww=6
		#try:
		if ww > 1:
			contextLabs={'title':_name,'year':_year,'img':_img,'fanart':_fanart,'country':_Country,'url':_Url,'plot':_plot,'genres':_Genres,'site':_site,'subfav':_subfav,'section':_section,'todoparams':_ToDoParams,'commonid':_commonID,'commonid2':_commonID2}
			##contextLabs={'title':_name,'year':'0000','url':_url,'img':img,'fanart':fimg,'DateAdded':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}
			contextMenuItems=ContextMenu_Favorites(contextLabs)
			contextMenuItems.append( ('Empty List','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'cFavoritesEmpty','site':site,'section':section,'subfav':subfav}) ) )
			#contextMenuItems=[]
			_title=wwA(_title,ww); 
			_addon.add_directory(pars,{'title':_title,'plot':_plot},is_folder=True,fanart=fimg,img=img,total_items=ItemCount,contextmenu_items=contextMenuItems)
		#except: pass
		#
	#
	if 'movie' in section.lower(): content='movies'
	else: content='tvshows'
	set_view(content,view_mode=int(addst('tvshows-view'))); eod()


### ############################################################################################################
### ############################################################################################################
def DoSearch_Post(title='',Url='/search/results.php'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	#deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','+'); 
	deb('Searching for',title); #ListShows( Url+( title.replace(' ','+') ) ); 
	deb('Url',Url); html=messupText(nolines(nURL(Url,method='post',form_data={'search':title,'page':'','hidden_page':'','valider':'GO'})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: return
	ListShowsH(Url,html)
	##
def DoSearch(title='',Url='/search/'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','%20'); 
	deb('Searching for',title); 
	##
	if ('_s_' in Url) or ('%s' in Url): Url=Url.replace('_s_','%s'); doUrl=Url % ( title.replace(' ','%20') )
	else: doUrl=Url + ( title.replace(' ','%20') )
	ListShows( doUrl ,'','html'  ); 
	##
def SpecialMenu(url):
	try: 
		if not '://' in url: html=common._OpenFile(TPapp(url))
		else: html=nURL(url)
		html=html.replace('\n','').replace('\r','').replace('\a','').replace('\t',''); data=eval(html); 
	except: data=[]
	iC=len(data); 
	if iC > 0:
		for (tag1,pars,tag2,labs) in data:
			img=pars['img'].replace('https://','http://'); fimg=pars['fimg'].replace('https://','http://'); 
			if fimg.lower()=='[fanart]': fimg=fanartSite
			debob(['pars',pars,'labs',labs]); 
			try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
			except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def DevFeaturedMenu():
	data=[]; 
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/91813392-05eb-486c-ba35-588c3d83f194/6xz69ho3twFsdxSTn7LD', 'roomslug': 'scifi-and-stuff', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/011/044/original/scifi-and-stuff-background_1403478667.jpg?1403478667', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/011/044/cinematic/scifi-and-stuff_1407528717.jpg?1407528717', 'title': 'scifi and stuff', 'url': '/scifi-and-stuff', 'type': 'js', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': '91813392-05eb-486c-ba35-588c3d83f194'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]scifi and stuff[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/a39f295f-5d51-4ecc-a7a9-976753f54594/ryhNcYybmfogwszSuNKH', 'roomslug': 'wikids-sci-fi-network', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/011/846/original/wikids-sci-fi-network-background_1406776905.jpg?1406776905', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/011/846/cinematic/wikids-sci-fi-network_1407994668.jpg?1407994668', 'title': 'wikids sci-fi network', 'url': '/wikids-sci-fi-network', 'type': 'js', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': 'a39f295f-5d51-4ecc-a7a9-976753f54594'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]wikids sci-fi network[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/c7bedc20-0bfe-4c25-bcfc-87724433a0d2/veHUPayVdZwrAFw4dnFU', 'roomslug': 'liaoalan1', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/014/794/original/liaoalan1-background_1407508549.jpg?1407508549', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/014/794/cinematic/liaoalan1_1407507250.jpg?1407507250', 'title': 'liaoalan1', 'url': '/liaoalan1', 'type': 'html', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': 'c7bedc20-0bfe-4c25-bcfc-87724433a0d2'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]liaoalan1[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	iC=len(data)
	for (tag1,pars,tag2,labs) in data:
		img=pars['img']; fimg=pars['fimg']; #debob(['pars',pars,'labs',labs]); 
		try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
		except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def BrowseMenu_FetchCats(Url='/browse',zz=[],d=[]):
	if (not '//' in Url) and (not '://' in Url) and (not mainSite in Url) and (not mainSite2 in Url) and (not mainSite3 in Url) and (not mainSite4 in Url): Url=mainSite+Url
	if ('//' in Url) and (not '://' in Url): Url='http:'+Url
	html=messupText(nolines(nURL(Url,headers={'Referer':mainSite})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: debob("No html found."); return d
	zz=re.compile('<div class="browseTab browseTabAccent(?:Selected)?" id="browseBtn[0-9A-Za-z]+" onclick="Browse\.[0-9A-Za-z]+\(\);"><img src="(/img/cat_.+?_white.png)" class="cat_img"/>\s*(.+?)\s*</div').findall(html.replace('</div>','</div\n\r\a>'))
	
	return zz
def BrowseMenu(Url='/browse',zz=[]):
	#zz=BrowseMenu_FetchCats(Url)
	
	zz.append("Misc")
	zz.append("People")
	zz.append("Nature")
	zz.append("Creative")
	zz.append("Music Cafe")
	zz.append("News & Tech")
	zz.append("Lifestyles")
	zz.append("Espanol")
	
	#zz.append("Vapers")
	#zz.append("Breakers")
	#zz.append("Gamers")
	_addon.add_directory({'mode':'BrowseCat3','site':site,'cat':'','type':'php'},{'title':AFColoring('All')},is_folder=True,fanart=fanartSite,img=(mainSite+'/img/cat_all_white.png'))
	for z in zz: 
		nonTitle=z.lower().replace(' ','').replace('&','')
		catName=nonTitle.replace('musiccafe3','music_cafe').replace('newstech','news_tech')
		pars={'mode':'BrowseCat3','site':site,'cat':catName,'type':'php'}; 
		img=(mainSite+'/img/cat_%s_white.png' % nonTitle.replace('musiccafe','music'))
		#img=(mainSite+'/img/cat_%s.png' % nonTitle)
		_addon.add_directory(pars,{'title':AFColoring(z)},is_folder=True,fanart=fanartSite,img=img); 
		#_addon.add_directory(pars,{'title':AFColoring(z)},is_folder=True,fanart=fanartSite,img=psgn('cat '+z.lower())); 
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'popular','type':'js'},{'title':AFColoring('Popular')},is_folder=True,fanart=fanartSite,img=psgn('popular'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'entertainment','type':'js'},{'title':AFColoring('Entertainment')},is_folder=True,fanart=fanartSite,img=psgn('entertainment'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'gaming','type':'js'},{'title':AFColoring('Gaming')},is_folder=True,fanart=fanartSite,img=psgn('gaming'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'music','type':'js'},{'title':AFColoring('Music')},is_folder=True,fanart=fanartSite,img=psgn('music'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'social','type':'js'},{'title':AFColoring('Social')},is_folder=True,fanart=fanartSite,img=psgn('social'))
	set_view('list',view_mode=addst('default-view')); eod()
	##
def TopBarMenu(Url='/app/topbar.php?s=vl',zz=[]):
	#zz=BrowseMenu_FetchCats(Url)
	
	zz.append("Misc")
	zz.append("People")
	zz.append("Nature")
	zz.append("Creative")
	zz.append("Music Cafe")
	zz.append("News & Tech")
	zz.append("Lifestyles")
	zz.append("Espanol")
	
	#zz.append("Vapers")
	#zz.append("Breakers")
	#zz.append("Gamers")
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'','type':'php'},{'title':AFColoring('All')},is_folder=True,fanart=fanartSite,img=(mainSite+'/img/cat_all_white.png'))
	for z in zz: 
		nonTitle=z.lower().replace(' ','').replace('&','')
		catName=nonTitle.replace('musiccafe','music_cafe').replace('newstech','news_tech')
		pars={'mode':'BrowseCat','site':site,'cat':catName,'type':'php'}; 
		img=(mainSite+'/img/cat_%s_white.png' % nonTitle.replace('musiccafe','music'))
		#img=(mainSite+'/img/cat_%s.png' % nonTitle)
		_addon.add_directory(pars,{'title':AFColoring(z)},is_folder=True,fanart=fanartSite,img=img); 
		#_addon.add_directory(pars,{'title':AFColoring(z)},is_folder=True,fanart=fanartSite,img=psgn('cat '+z.lower())); 
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'popular','type':'js'},{'title':AFColoring('Popular')},is_folder=True,fanart=fanartSite,img=psgn('popular'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'entertainment','type':'js'},{'title':AFColoring('Entertainment')},is_folder=True,fanart=fanartSite,img=psgn('entertainment'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'gaming','type':'js'},{'title':AFColoring('Gaming')},is_folder=True,fanart=fanartSite,img=psgn('gaming'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'music','type':'js'},{'title':AFColoring('Music')},is_folder=True,fanart=fanartSite,img=psgn('music'))
	#_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'social','type':'js'},{'title':AFColoring('Social')},is_folder=True,fanart=fanartSite,img=psgn('social'))
	set_view('list',view_mode=addst('default-view')); eod()
	##
def SectionMenu():
	#common.check_database() #Checks rather the Database needs initialized or updated.
	##import splash_highway as splash; #splash.do_My_Splash(_addon.get_fanart(),2,False); 
	##splash.do_My_Splash(HowLong=5,resize=False); 
	SpecialCODE=addst('special-code',''); LocalLists=[]; 
	_addon.add_directory({'mode':'BrowseMenu','site':site},{'title':AFColoring('Browse')},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	_addon.add_directory({'mode':'TopBarMenu','site':site},{'title':AFColoring('Top Bar')},is_folder=True,fanart=fanartSite,img=psgn('topbar'))
	
	#_addon.add_directory({'mode':'BrowseCat2','site':site,'cat':'rooms','type':'js|featured'},{'title':AFColoring('Featured')},is_folder=True,fanart=fanartSite,img=psgn('browse featured'))
	#_addon.add_directory({'mode':'SpecialMenu','url':'http://raw.github.com/HIGHWAY99/plugin.video.streamup/master/lists/DevsFeaturedList.txt','site':site},{'title':AFColoring("Dev's Featured List")},is_folder=True,fanart=fanartSite,img=psgn('browse devs featured'))
	
	#LocalLists.append(['MyPicksList.txt','My Picks List','browse my picks list'])
	#LocalLists.append(['LocalList.txt','Local List','browse local list'])
	##LocalLists.append(['','','browse'])
	#for (urlA,TiTLE,iMg) in LocalLists:
	#	urlB=TPapp(urlA)
	#	if isFile(urlB)==True:
	#		html=common._OpenFile(urlB)
	#		if len(html) > 10:
	#			_addon.add_directory({'mode':'SpecialMenu','url':urlA,'site':site},{'title':AFColoring(TiTLE)},is_folder=True,fanart=fanartSite,img=psgn(iMg))
	
	#if SpecialCODE==ps('special-code'):
	#	_addon.add_directory({'mode':'DevFeaturedMenu','site':site},{'title':AFColoring("Dev's Featured List[CR][Hard Coded]")},is_folder=True,fanart=fanartSite,img=psgn('browse devs featured'))
	
	#_addon.add_directory({'mode':'Search','site':site,'url':'/search/'},{'title':AFColoring('Search')+cFL(' Channels',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search'))
	#_addon.add_directory({'mode':'Search','site':site,'url':'/search/_s_/users.js'},{'title':AFColoring('Search')+cFL(' People',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search user'))
	#_addon.add_directory({'mode':'History101','site':site,'url':''},{'title':AFColoring('History')+cFL(' 101',colorB)},is_folder=True,fanart=fanartSite,img=psgn('history 101'))
	
	#
	#if SpecialCODE==ps('special-code'):
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section             },{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.1.name'),colorB)},fanart=fanartSite,img=psgn('favorites 1'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'2'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.2.name'),colorB)},fanart=fanartSite,img=psgn('favorites 2'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'3'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.3.name'),colorB)},fanart=fanartSite,img=psgn('favorites 3'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'4'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.4.name'),colorB)},fanart=fanartSite,img=psgn('favorites 4'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'5'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.5.name'),colorB)},fanart=fanartSite,img=psgn('favorites 5'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'6'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.6.name'),colorB)},fanart=fanartSite,img=psgn('favorites 6'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'7'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.7.name'),colorB)},fanart=fanartSite,img=psgn('favorites 7'))
	###
	#if (len(addst("LastShowListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'ListEpisodes','url':addst("LastShowListedURL"),'title':addst("LastShowListedNAME"),'imdb_id':addst("LastShowListedIMDBID"),'img':addst("LastShowListedIMG"),'fimg':addst("LastShowListedFANART")}; 
	#	title=AFColoring(addst("LastShowListedNAME"))+CR+cFL('[Last Show]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastShowListedFANART"),img=addst("LastShowListedIMG"),is_folder=True); 
	#if (len(addst("LastEpisodeListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'GetMedia','url':addst("LastEpisodeListedURL"),'title':addst("LastEpisodeListedNAME"),'imdb_id':addst("LastEpisodeListedIMDBID"),'img':addst("LastEpisodeListedIMG"),'fimg':addst("LastEpisodeListedFANART"),'stitle':addst("LastEpisodeListedSTITLE"),'etitle':addst("LastEpisodeListedETITLE"),'e':addst("LastEpisodeListedEpNo"),'s':addst("LastEpisodeListedSNo"),'e2':addst("LastEpisodeListedEpNo2")}; 
	#	title=AFColoring(addst("LastEpisodeListedNAME"))+CR+cFL('[Last Episode]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastEpisodeListedFANART"),img=addst("LastEpisodeListedIMG"),is_folder=True); 
	###
	#_addon.add_directory({'mode':'About','site':site,'section':section},{'title':AFColoring('About')},is_folder=True,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	###
	set_view('list',view_mode=addst('default-view')); eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	try: debob({'mode':mode,'url':url,'title':addpr('title','')})
	except: pass
	if (mode=='SectionMenu'): 					SectionMenu()
	elif (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
	elif (mode=='SubMenu'): 						SubMenu()
	elif (mode=='SpecialMenu'): 				SpecialMenu(url)
	elif (mode=='DevFeaturedMenu'): 		DevFeaturedMenu()
	elif (mode=='BrowseMenu'): 					BrowseMenu()
	elif (mode=='TopBarMenu'): 					TopBarMenu()
	##																 #ListShows(Url,Page='',TyPE='js',idList='[]', csrfToken='')
	elif (mode=='ListShows'): 					ListShows(url,addpr('page',''),addpr('type',''),addpr('idlist',''),addpr('csrfToken',''))
	elif (mode=='BrowseCat'): 					ListShows(mainSite+"/app/topbar.php?s=vl%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat2'): 					ListShows(mainSite+"/app/topbar.php?s=%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat3'): 					ListShows(mainSite+"/browse/%s?a=mvn" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat4'): 					ListShows(mainSite+"/browse/%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='Search'):							DoSearch(addpr('title',''),url)
	elif (mode=='History101'):					History101()
	elif (mode=='PlayLiveStream'): 			PlayLiveStream(url,addpr('title',''),addpr('img',''),addpr('channel',''),addpr('roomid',''),addpr('roomslug',''),addpr('plot',''),addpr('live',''),addpr('streamurl',''),addpr('streamkey',''),addpr('youtubeid',''),addpr('sourcetype','show'))
	#
	elif (mode=='BrowseUrl'): 					XBMC_System_Exec('"%s"' % url)
	elif (mode=='FavoritesList'): 			Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='About'): 							eod(); About()
	elif (mode=='PlayPICTURES'): 				PlayPictures(url)
	elif (mode=='PlayURL'): 						PlayURL(url)
	elif (mode=='PlayURLs'): 						PlayURLs(url)
	elif (mode=='PlayURLstrm'): 				PlayURLstrm(url)
	elif (mode=='PlayFromHost'): 				PlayFromHost(url)
	elif (mode=='PlayVideo'): 					PlayVideo(url)
	elif (mode=='PlayItCustom'): 				PlayItCustom(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='PlayItCustomL2A'): 		PlayItCustomL2A(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='Settings'): 						_addon.addon.openSettings() # Another method: _plugin.openSettings() ## Settings for this addon.
	elif (mode=='ResolverSettings'): 		import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='ResolverUpdateHostFiles'):	import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='TextBoxFile'): 				TextBox2().load_file(url,addpr('title','')); #eod()
	elif (mode=='TextBoxUrl'):  				TextBox2().load_url(url,addpr('title','')); #eod()
	elif (mode=='Download'): 						
		try: _addon.resolve_url(url)
		except: pass
		debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))])
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true')))
	elif (mode=='toJDownloader'): 			SendTo_JDownloader(url,tfalse(addpr('useResolver','true')))
	elif (mode=='cFavoritesEmpty'):  		fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh"); 
	elif (mode=='cFavoritesRemove'):  	fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  			fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	elif (mode=='AddVisit'):							
		try: visited_add(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='RemoveVisit'):							
		try: visited_remove(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='EmptyVisit'):						
		try: visited_empty(); RefreshList(); 
		except: pass
	elif (mode=='refresh_meta'):				refresh_meta(addpr('video_type',''),addpr('title',''),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); #SectionMenu()
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
