//------------------------------------
//
//	ENGAGE.TBLANK.JS
//
//	Automatically shows a popup on
//	external link clicks then sets
//	cookie to remember the choice.
//
//	Author: 	Engage Interactive
//	Requires:	jquery 1.4.x
//				engage.tblank.css
//
//	Copyright (c) 2010 Engage Interactive (engageinteractive.co.uk)
//	Dual licensed under the MIT and GPL licenses:
//	http://www.opensource.org/licenses/mit-license.php
//	http://www.gnu.org/licenses/gpl.html
//
//------------------------------------


// Activate the plugin
$(document).ready(function() {
	$('body').tblank();
});

(function($){$.fn.tblank=function(options){var defaults={internal:'internal',external:'external',cookie:true,cookieName:'engage.tblank',useBy:365,popupText:'<p>You&rsquo;ve clicked an external link, how would you like to open it?</p><p>We will remember your answer for next time.</p>',onOpen:function(){},onSame:function(){},onNew:function(){},onCancel:function(){},devMode:false},settings=$.extend({},defaults,options);$('a[href*="http://"]:not([href*="'+location.hostname+'"]):not([class*="'+settings.internal+'"]):not([class*="'+settings.external+'"]):not([id*="ep_new"])').live('click',function(){if(settings.cookie==true){c=$.cookie(settings.cookieName);if(c=='new'){window.open($(this).attr('href'));}else if(c=='same'){window.location.href($(this).attr('href'));}else{external(this.href,$(this).attr('title'));}}else{external(this.href,$(this).attr('title'));}
return false;});function external(url,title){html='<div id="externalPopup"><div id="ep_container"><h3 id="ep_title"><em></em></h3>'+settings.popupText+'<ul><li><a href="#" id="ep_new" class="'+settings.external+'">New window</a></li><li><a href="#" id="ep_same" class="'+settings.internal+'">Same window</a></li><li><a href="#" id="ep_cancel" title="Cancel this action and return to the site">Cancel</a></li></ul></div><span id="ep_background"></span></div>';$('body').append(html);$('#ep_title em').before(title).text(url);$('#ep_new').attr('href',url).attr('title','Open '+title+' in a new window');$('#ep_same').attr('href',url).attr('title','Open '+title+' in the same window');$('#ep_background').css({opacity:0.8});$('#externalPopup').show();ie6('open');settings.onOpen.call(this);}
$('#ep_new').live('click',function(){settings.onNew.call(this);$.cookie(settings.cookieName,'new',{expires:settings.useBy});$('#externalPopup').remove();ie6('close');window.open($(this).attr('href'));return false;});$('#ep_same').live('click',function(){settings.onSame.call(this);$.cookie(settings.cookieName,'same',{expires:settings.useBy});});$('#ep_cancel, #ep_background').live('click',function(){settings.onCancel.call(this);$.cookie(settings.cookieName,null);$('#externalPopup').remove();ie6('close');return false;});$('a.external').live('click',function(){window.open($(this).attr('href'));return false;});function ie6(act){if($.browser.msie&&$.browser.version.substr(0,1)<7){if(act=='open'){pageH=$(window).height();pageY=$(window).scrollTop();$('#externalPopup').css({position:'absolute',height:pageH,top:pageY});$('html, body').css({overflow:'hidden'});$('#ep_background').css({width:$(window).width(),height:pageH});}else if(act=='close'){$('html, body').css({overflow:''});}}}
if(settings.devMode==true){$('body').prepend('<a href="#" id="ep_devDelete">Delete cookie</a> <a href="#" id="ep_devShow">Show cookie</a>');}$('#ep_devDelete').live('click',function(){$.cookie(settings.cookieName,null);});$('#ep_devShow').live('click',function(){alert($.cookie(settings.cookieName));});};})(jQuery);


//------------------------------------
//
//	Cookie plugin
//
//	Copyright (c) 2006 Klaus Hartl (stilbuero.de)
//	Dual licensed under the MIT and GPL licenses:
//	http://www.opensource.org/licenses/mit-license.php
//	http://www.gnu.org/licenses/gpl.html
//
//------------------------------------

eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('o.5=q(b,9,2){7(h 9!=\'x\'){2=2||{};7(9===j){9=\'\';2=$.v({},2);2.3=-1}4 3=\'\';7(2.3&&(h 2.3==\'m\'||2.3.l)){4 6;7(h 2.3==\'m\'){6=t u();6.s(6.w()+(2.3*r*p*p*z))}k{6=2.3}3=\'; 3=\'+6.l()}4 8=2.8?\'; 8=\'+(2.8):\'\';4 a=2.a?\'; a=\'+(2.a):\'\';4 c=2.c?\'; c\':\'\';d.5=[b,\'=\',E(9),3,8,a,c].y(\'\')}k{4 e=j;7(d.5&&d.5!=\'\'){4 g=d.5.F(\';\');D(4 i=0;i<g.f;i++){4 5=o.C(g[i]);7(5.n(0,b.f+1)==(b+\'=\')){e=B(5.n(b.f+1));G}}}A e}};',43,43,'||options|expires|var|cookie|date|if|path|value|domain|name|secure|document|cookieValue|length|cookies|typeof||null|else|toUTCString|number|substring|jQuery|60|function|24|setTime|new|Date|extend|getTime|undefined|join|1000|return|decodeURIComponent|trim|for|encodeURIComponent|split|break'.split('|'),0,{}))