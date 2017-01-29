---
layout: post
title: "How to Create a Custom Email Signature for Mail"
date: 2016-06-27 10:54:23 -0700
---

Personal email signatures are a great way to add a personal touch.
Many know of and how to already do this in their email client of choice.
Mail in OS X has some great options for customizing your personal signature and even allows for the creation of multiple and the formatting of the text and content.  
In an effort to add some creative and technical merit to my signature I have created a custom HTML signature. Links, formatted text and even pictures are already supported in the OS X native Mail client. What an HTML signature provides me is access to a wider range of format customization through inline CSS.  

I would like two email signatures, one for my office email with my day job and one for my personal email such as that connected to [this site](www.Jerad.xyz). I would like each email to have a branded experience so that someone reading an email from my office account will feel like they are reading something composed by my office and someone reading an email from my personal account feels connected to the content herein where I write about my endeavors into such things. I also want my signature to be clickable, sending the reader to a relevant location or opening up an email template readily addressed to myself.  

What I want in an email signature:
- Two emails
  - Professional
  - Personal
- Branded experience
- Hot spaces for active clicking
  - Email link
  - Link to website


```html
<style type="text/css">
	a.link{margin:0;padding:0;border:none;text-decoration:none;}
</style>

<br />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="format-detection" content="telephone=no">

<table width='320' id="sig" cellspacing='0' cellpadding='0' border-spacing='0' style="width:320px;margin:0;padding:0;">
	<tr>
		<td width="86" style="width:86px;margin:0;padding:0;">
			<a href='[Desired-link-destination]' style="border:none;text-decoration:none;">
        <img moz-do-not-send="true" src="[Address-of-Image]" alt="GiantUser" style="border:none;width:86px;">
      </a>
		</td>

  	<td width="10" style="width:10px;min-width:10px;max-width:10px;margin:0;padding:0;">&nbsp;</td>
    <!-- <td width="10" style="width:10px;min-width:10px;max-width:10px;margin:0;padding:0;border-left:1px solid #e0e0e0">&nbsp;</td> -->

		<td valign='top' style="margin:0;padding:0;">
			<table id="sig2" cellspacing='0' cellpadding='0' border-spacing='0' style="padding:0;margin:0;font-family:'Lucida Grande',sans-serif;font-size:12px;color:#b0b0b0;border-collapse:collapse;-webkit-text-size-adjust:none;">
				<tr style="margin:0;padding:0;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<strong><a href="mailto:[Your-Email-Address]" style="border:none;text-decoration:none;color:#049cdb;"><span style="color:#049cdb">Your Name</span></a></strong><span style="color:e0e0e0;">,</span>
						<span style="color:#b0b0b0;">Job Title or Position</span>
					</td>
				</tr>
				<tr style="margin:0;padding:0;color:#b0a49b;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<a href="[Office-or-Personal-Website]" style="border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">[Office-or-Personal-Website-Name]<span style="color:#e0e0e0">.</span>com</span></a><span style="color:e0e0e0;">,</span>
						<a href="http://g.co/maps/wnbde [Google-Map-To-Open-Showing Office-Location]" style="border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">New York[Text-Location-Of-Office-That-Opens-Google-Map-Link]</span></a>
					</td>
				</tr>

				<tr style="margin:0;padding:0;color:#b0a49b;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<a href="tel:[Phone Number]" style="margin:0;padding:0;border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">347</span><span style="color:#e0e0e0">.</span><span style="color:#b0b0b0">688</span><span style="color:#e0e0e0">.</span><span style="color:#b0b0b0">7226</span></a>
						<span style="color:e0e0e0;">&bull;</span>
						<a href="http://twitter.com/[Twitter-Handle]" style="margin:0;padding:0;border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">Twitter</span></a>
					</td>
				</tr>
			</table>
		</td>
	<tr>
</table>
<br />
&nbsp;
```

### Current Draft
Here is what my current draft of a custom HTML email signature for the OS X Mail client:

<style type="text/css">
	a.link{margin:0;padding:0;border:none;text-decoration:none;}
</style>

<br />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="format-detection" content="telephone=no">

<table width='320' id="sig" cellspacing='0' cellpadding='0' border-spacing='0' style="width:320px;margin:0;padding:0;">
	<tr>
		<td width="86" style="width:86px;margin:0;padding:0;">
			<a href='http://Jerad.xyz' style="border:none;text-decoration:none;">
        <img moz-do-not-send="true" src="/images/JA.png" alt="MySite" style="border:none;width:86px;">
      </a>
		</td>

  	<td width="10" style="width:10px;min-width:10px;max-width:10px;margin:0;padding:0;">&nbsp;</td>
    <!-- <td width="10" style="width:10px;min-width:10px;max-width:10px;margin:0;padding:0;border-left:1px solid #e0e0e0">&nbsp;</td> -->

		<td valign='top' style="margin:0;padding:0;">
			<table id="sig2" cellspacing='0' cellpadding='0' border-spacing='0' style="padding:0;margin:0;font-family:'Lucida Grande',sans-serif;font-size:12px;color:#b0b0b0;border-collapse:collapse;-webkit-text-size-adjust:none;">
				<tr style="margin:0;padding:0;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<strong><a href="mailto:ir@Jerad.xyz" style="border:none;text-decoration:none;color:#049cdb;"><span style="color:#049cdb">Jerad Acosta</span></a></strong><span style="color:e0e0e0;">,</span>
						<span style="color:#b0b0b0;">Reckoner</span>
					</td>
				</tr>
				<tr style="margin:0;padding:0;color:#b0a49b;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<a href="http://Jerad.xyz" style="border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">Jerad<span style="color:#e0e0e0">.</span>XYZ</span></a><span style="color:e0e0e0;">,</span>
						<a href="https://goo.gl/maps/H3iGyTgo8vJ2" style="border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">San Francisco</span></a>
					</td>
				</tr>

				<tr style="margin:0;padding:0;color:#b0a49b;">
					<td style="margin:0;padding:0;font-family:'Lucida Grande',sans-serif;white-space:nowrap;">
						<a href="tel:+1-760-840-0524" style="margin:0;padding:0;border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">760</span><span style="color:#e0e0e0">.</span><span style="color:#b0b0b0">840</span><span style="color:#e0e0e0">.</span><span style="color:#b0b0b0">0524</span></a>
						<span style="color:e0e0e0;">&bull;</span>
						<a href="http://twitter.com/irJERAD" style="margin:0;padding:0;border:none;text-decoration:none;color:#b0b0b0;"><span style="color:#b0b0b0">Twitter</span></a>
					</td>
				</tr>
			</table>
		</td>
	<tr>
</table>
<br />
&nbsp;
