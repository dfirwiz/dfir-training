# Day 2 batch03 — displayed11/12 — 2026-11-06

## Authorized scope and preserved baseline

Latest main128893f7c29718fbbe3d3c955bffba7d13220eb8 checked through GitHub connector and native fetch. Worktree initially clean, no active_batch. Firstday26/second-day1–10 already verified,36published. Do not repeat old10. Original numericID8 is displayed11; numericID9 is displayed12. Course title retained, other course/home content preserved. SMTP139–160 is too broad for one detailed note alongside the exercise: split only unpublished plannedSMTP into12=139–149,13=d2-09b150–155,14=d2-09c156–160; following planned original10/11/12 now15/16/17. No published numbers/IDs/URLs/prose changed. Wholecourse unfinished; automation remainslocal/active, cloudmigration unverified. Continued user request during execution retained this objective.

## Source access and correspondence

Actual designated volume2 D:/SANS/SEC450/450_2022 (02).pdf reopened with pypdf: printed137–148/PDF139–150, then printed149/PDF151 separately; all13pages read. Initial console cp949 encoding error occurred after private extraction saved, then rerun with UTF8 stdout and alltext observed. Printed149–161 headings read solely for future splitting, not completed future content. Private full extraction tmp/day2-mail-source/batch03.txt. Poppler printed142/PDF144 and149/PDF151 rendered and visually inspected, source-mta.png/source-received.png; Symbol/ArialUnicode displayfont warnings crosschecked against extractedtext, no exactfontreproduction claim. No sourcePDF/screens/rawfulltext published.

Inspected designated D:/SANS/SEC450 tree and relatedrecords: fivevolumes, PDF2022duplicates and volume1docx. No separately accessible originalworkbook/wiki/VM/incidentPCAP obtained in these scopedlocations; do not generalize to whole-device absence. Maintextbook supplies topic sequence;137–138 only redirect to separateexercise, not full procedure. Own11 is explicitly independentpractice, not originalworkbook completion. Own12 message and SMTPdialog are distinct handmade artifacts, not a real captured message/session pair.

| Original printed pages | Source learning items | Independent coverage |
| --- | --- | --- |
|137–138|Roadmap and HTTP/HTTPS separateworkbookexercise pointer|11§1–21 independentpacket/reportcorrelation; scope/access limits§1/3/4; review§22. No originalstepsinvented.|
|139–141|Email module roadmap; MUA/MSA/MTA/MDA submission/relay/storage/access andwebmail|12§1–5; deliveryrolesSVG; logicalroles,webHTTPSvssubsequentSMTP,ports/currentTLSaccess supplement|
|142|Intermediate/borderMTA/MX and outbound/inboundroles; TCPclaim; SPFbridge|12§3–7,§19–21; MXpreference/absent/nullMX; trustboundary/TCPpeer≠person. SPFbridge deliberately continues13, notclaimedcompletehere.|
|143|SMTP/EHLO/envelope/DATA/status/text/case assertions|12§8–14; fictionaltranscript. Correct MAILFROM≠headerFrom;RCPTTO≠headerTo; 354vsfinal250;dotstuffing/case/localpart/SMTPUTF8/STARTTLSconditions.|
|144–145|Trace/messageheaders/body andsamplemessage/MIME/encoding|12§10/15/17–19/27; nooriginalsamplecopied; optional/emptybody and MIMEalternatives notallattachmentsbase64; messageIDnotauth.|
|146|Outlook/Gmail source viewing|12§16 currentmanufacturerpaths separatedclassic/new/web; header-only/bodyHTMLsource≠fulloriginal; noactualGUIexport.|
|147–148|Receivedprepend/order/relaychain/timezones/webmailclientIP/whichlinestrust|12§19–26/28; preserveorder, UTC3+3seconds, externalearlierclaim vs selectedboundary, knownprovidername≠allprevioushoptrust; TCPnotabsoluteidentityguarantee.|
|149|ReceivedfromEHLO/PTR/IP/by/with/id/for/time|12§19–21/23/27; simplefixedformparsed, optionalproductsyntaxnotuniversal; connectionpeer/directlog/claimednames distinguished.|

No unassigned conceptual item within137–149. Originalworkbook execution notverified. RemainingSMTPauthentication150–160 remainsplanned; nextactualreread needed.

## Official sources actually consulted 2026-11-06

- RFC5321 https://www.rfc-editor.org/rfc/rfc5321.html andinfo status page: commands/response/acceptancehandoff,ReceivedfromTCPpeer andEHLOclaim,MXpreference/implicitMX,case/localpart/envelopevsmessage. Avoid absolutecannotspoof/personclaim and blanketmessagefieldsasMAIL/RCPT.
- RFC5322 https://www.rfc-editor.org/rfc/rfc5322.html andinfo: fieldstructure/folding/unfolding/optionalbody/messages; preservedoriginalsource ratherthanscreenshotascomplete.
- RFC6409 https://www.rfc-editor.org/rfc/rfc6409.html submission587vsrelay25; RFC8314 https://www.rfc-editor.org/rfc/rfc8314.html implicitTLS465/IMAP993/POP995, TLSconditionsnotportguarantee. HistoricalminimumTLSversionin8314notrepeatedascurrentrecommendation.
- RFC7505 https://www.rfc-editor.org/rfc/rfc7505.html NullMXdistinctfromempty/noMXlookup.
- RFC3207 https://www.rfc-editor.org/rfc/rfc3207.html STARTTLSreset/reEHLO/hopprotection, notendtoendguarantee.
- RFC6531 https://www.rfc-editor.org/rfc/rfc6531.html SMTPUTF8internationalizedmailundernegotiatedconditions; noallSMTPASCIIonlyclaim.
- RFC2045 https://www.rfc-editor.org/rfc/rfc2045.html MIMEencodingvsencryption; RFC2046 https://www.rfc-editor.org/rfc/rfc2046.html#section-5.1.4 multipartalternative semantics, nottwoindependentmails/files.
- RFC3848 https://www.rfc-editor.org/rfc/rfc3848.html withESMTPSAmeaning/hopreportnotcryptographicidentity/safety. RFC8601 https://www.rfc-editor.org/rfc/rfc8601.html trustboundary references corroborateproducer/consumer/provenanceprinciple; detailedSPFDKIMDMARC notcoveredthisbatch.
- Microsoft https://support.microsoft.com/en-us/outlook/view-internet-message-headers-in-outlook actualnew/webMoreactions→View→Viewmessagedetails;classicownwindowFile→Properties→Internetheaders. Google https://support.google.com/mail/answer/29436?hl=en More→Showoriginal; noactualappactions,exports,externalheaderpastingperformed.
- Python https://docs.python.org/3.12/library/email.parser.html actualBytesParsercapability; docs3.12.16 vsruntime3.12.14 distinguished. https://github.com/kbandla/dpkt projectcapability checked, ownfixedfixtureparsermuchnarrower. Existingdpkt1.9.8 usedwithoutinstallation.
- Wireshark https://wiki.wireshark.org/TLS conditionsrechecked; https://www.wireshark.org/docs/dfref/h/http.html actualhttp.host/http.request.method fields1.0.0–4.6.9 referenced, noforeverlatestclaim. Filterexplicitlyunexecuted.

## Actually executed independent examples

New3lab11files(case/coordinator/README) reuseunchangedold08inspect_http and2harmlessPCAPs. New5lab12files(message.eml/tracepolicy/inspect_mail/smtp-session/README). message.emlrawASCII CRLF retained through -textgitattribute; noattachment/malware/realaddresses. AllfictionalIPsdocumentranges/.exampledomains. Onlylocalreads/calculations/output. Nooriginalworkbook/VM,livecapture/SMTPsend/URLvisit/DNSlookup/authentication/TLSnegotiation/decrypt/keys/CAinstall/JARM/certvalidation/HTMLrender/attachmentexecution/message/purchase.

check_day02_batch03_examples.py actual25runs passed. Input11filesSHA256unchanged (8new+3reused). Firsthelperrun encountered transientPermissionErroroverwritingvariant.eml afterpriorreads; isolateduniquevariantnamesfixedit, full25rerunpassed. Noauto-reviewrejection ornewinstallation.

HTTPfull3frames/headerbody35/decode15, textTrainingonly plusLF;decodedSHA256571143bbfd4e9e23772d8174a1f60be72d69923ed8b4a8c4744081059cd4203f, wholecapturee640f5c16b53895fe93f180d3ce44187e63ac4f1b57043754fe2ce601c582cd7. E1reportedhashtrue/E2false,reportedtimesUTC09:00:05/09:00:07 vsfictionalreference09:00:00→5/7seconds. NotPCAPtimestampcorrelation. Missingtail2framesbody10/missing25→bothhashcomparisonsnull,notfalse. Executionclaimchangesdonotverifyexecution,reportorder/offsetequivalencechecks;invalidtimezone/hash/state/port/missingvisibility/contract/emptyreports rejected.

EmailrawSHA256f5e4ffa4080caa7f91eb23b30a9d0b354f25a0a4533bdb01e944f5bf25a7a8aa. ThreefoldedReceivedparsedtopfirstUTC10:00:04/10:00:01/09:59:58,interval3+3seconds. Index1edgeexpectedpeer198.51.100.40matchesbutauthority/person/authfalse. Lowerpeerchanged192.0.2.99leavesboundarycomparison;offsetequivalencepreservesintervals;wrongexpectedpeerfalse;changeindexdoesnotconferauthority;negativeinterval-2notautomaticforgery. Invalidboolean/outofrange/wrongreceiver/externalcontract/duplicateFrom/unsupportedbyform/IPv6syntaxrejected. MIMEleaftextplain/texthtmlonlyreported,norender. SMTPtranscriptmanualandnotparsed/executed;EMLnotcapturedfromit. Allincidentunresolved/externalactions0.

## Build and browser validation

Static40HTML/38published/36priorbodies/homeothercontent/numbering/IDs/links/anchors/HTMLnesting/inlinecode/downloads passed. New11=22sections77paragraphs3SVG2tables14immediateanswers;12=29sections98paragraphs3SVG2tables16immediateanswers. Total51sections175paragraphs4tables6SVG30Q&A. Six400pxoriginalSVG Koreanfontbounds[]/contactsheet visuallyinspected. Tables/codesinternaloverflowstylesretained.

Browserinventory changedthisexecution: IAB nowavailable, whereaspreviousbatch browsers[]. Localpreviewserver127.0.0.1:8767 startedhidden PID10744;actualdesktopinitial11header/sidebarnavigationviewed. Temporary390×844viewportused;11firstSVG actuallyloaded400naturalwidth/display335andvisuallyreadable. Pagewidth375≤390, tableclient343/scroll580 andcodeclient343/scroll390–483internalauto. Initialsnapshotbeforelazyimage scrollshowednatural0, lateractualfirstimage400; notclassifiedasbrokenwithoutviewporttrigger. Additional11/12SVG/table checksanddesktop12ongoing; finalresultwillbeappended,donotclaimallsectionsfullyvisuallyreviewed.

## Publication gate

Drafts built andlocallychecked; contentpublication/Actions/publicproof pending. Progress remainsday2completed1–10 withactive11/12. Onlyafterdeploymentsuccessandpublicresourcesmatchadvance1–12/clearactivebatch. Next13source150–155/14source156–160. Wholecourseunfinished,automationactive/local; do not claimcloudmigration.


## Final browser result and limit

During further11/12checks, CUA returned LocalbrowseruseisdisabledinWorksettings. Stoppedbrowserwork, sentrequiredcompletion_summary, didnotbypassorchangeusersettings. Actualcompleted:11desktopheader/sidebar screenshot;390×844mobilefirstoriginalSVG loadednatural400/display335andvisuallyinspected;11pagewidth375≤390/table343vs580/code343vs390–483internalauto. Browser12onlynavigatedtoanchors; nocaptured12visualverification orall6image-loadingclaim. Other11SVGsnotallbrowserinspected. All6staticKoreanfontbounds[]/contactsheetviewed,40HTMLstructureandrelativehref/anchorchecksverified. Temporaryviewportresetcouldnotbeperformedafteraccessdisabled; notclaimedreset. Browserinterruptiondoesnotblockauthorizedpublication; limitationsdisclosed. PreviewserverPID10744willbestoppedafterlocalQA.


Final source149crosscheck explicitly addedReceivedfor optional/single-path-notallrecipients/Bccscope to12§19. Sameparagraphcount; sourcecorrespondenceandHTMLrevalidated. Finalpublicationproof must use followup contentcommit, not initialdcd9778.


## Verified publication result2026-11-06

Publication9f932891aec7d287fe4d79c7932a69a645c2efa4;Actions42220896658completed/success. Public59resourcesHTTP200/contentmatch:40HTML/CSS/coursejson/6SVG/8newdownloads/3reuseddownloads. OriginalEMLCRLFand2PCAPsexactbytesmatched;othertextLFnormalizedmatched. Onlyafterproofadvancedday2display1–12/clearedactivebatch.36previousbodies/otherhomepagecontentpreserved. Next13original150–155/14original156–160,actuallyreopenandcurrentprimarychecksneeded. Partialbrowserlimitsasabove;originalworkbook/VM/liveSMTP/TLSunverified. Wholecourseunfinished,automationactive/local.
