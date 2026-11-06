# Second day7/8 — HTTP triage, headers and content evidence

Status: locally drafted, built, checked; remote publication/deployment/public proof pending. Do not advance completed progress until proof. Display7=id7,8=d2-07b. Preserve existing day1=26/day2old1–6:32 lesson bodies, published IDs/numbers/URLs and other course/home content. New total34 published.

## Source access and prior coverage audit

Designated volume2 actually accessible:182PDFpages/printed1–180, physical=printed+2. Actual read new printed107–138; completed new scope only107–123,124–138 read-ahead remains planned. Private source tmp/day2-http-source/new.txt/prior.txt/page-index.json never published. Newsource115/PDF117 and118/PDF120 rendered/viewed privately, Symbol/ArialUnicode substitution warnings cross-checked with extracted text. Source pictures/actual hostile addresses/payloads not republished or executed.

Before selecting next scope: actually reread original5–30, full earlier3–6 correspondence tables, old2publication record, all six public manuscript section headings and selected substantive1/2 sections on visibility/zero-trust/segmentation/compensating controls and flow/PCAP/formats/DoH. Original31–106 page-index headings checked against prior range mappings;31/50/51/85/86/87/88/106 source pages reread. This combines earlier actual full-range reads with current structural correspondence and selected rereads; not a fresh complete word-for-word reread of31–106 or all six manuscripts this turn.

| Original printed range | Existing lesson | Correspondence and retained corrections |
| --- | --- | --- |
| 5–17 | day2old1 sections1–13 | Roadmap/architecture/routers/zones/flow/switches/TAP-SPAN/firewalls/identity/zero-trust/segmentation/flat-network controls/summary. Actual5–17 fully reread. Existing body distinguishes location/capacity, active/passiveTAP, model-dependentSPAN, segmentation vs completezero-trust, modern endpoint controls. |
| 18–30 | day2old2 sections1–20 | Roadmap/data categories/NetFlow/TShark summaries/use cases/sensor/Zeek/PCAP/tools/UI/filters/follow conversation/summary. Actual18–30 fully reread; metadata/storage/limitedcapture/sampling/expandedflow/IPFIX/Npcap retained. Source28incorrectdns-and-tlsgeneralDoHclaim already expressly corrected in old2section16. |
| 31–50 | day2old3 sections1–20 | Earlier complete page-by-page DNS mapping in network-security-03-coverage-20261102.md; current headings + boundaries rechecked. TXT/TTL/cache/PTR/CNAME/recordtypes/multito-many/queryresponse/tool/quiz coverage retained. |
| 51–85 | day2old4 sections1–27 | Earlier complete mapping in network-security-04-coverage-20261102.md; current allsourceheadings/oldsectionheadings/boundaries rechecked. DNS traffic/forwarder/reputation/enrichment/tunnel/IDN/encryption/sensorlimits/independent cases. Currentcorrections retained. |
| 86–87 | day2old5 sections1–22 | Pointer to separately unavailable workbook/wiki; independent synthetic DNS PCAP practice, not original exercise completion. |
| 88–106 | day2old6 sections1–27 | 88roadmap rechecked,89–106 earlier detailed mapping in network-security-06-coverage-20261102.md; all currentheadings/summary rechecked. HTTP messages/methods/headers/status/body/gzip/HTTP2/3/WebSocket. Version-specific previous supplements retained. |

No unmapped conceptual range5–106 identified by this audit. Original separateworkbook steps/VM execution remain unverified; independent substitutes not silently counted as original lab completion. Accessible D:/SANS/SEC450 and PDF2022 contain5PDFs/duplicates andvolume1docx; related records andexisting ownlab05 checked. No separate originalworkbook/wiki/VM/incidentPCAP acquired in this inspected scope, not a claim of whole-system absence. Continue new107 without repeating existing6.

## New source correspondence and split

| Original printed page | New independent section coverage |
| --- | --- |
| 107roadmap | 7section1/8section1 and revised unpublished plan |
| 108HTTP attack phases | 7sections2–3, request/transport vs phishing/delivery/C2/exfiltration success |
| 109method selection | 7sections3/8–10/19–20, automated/manual purpose and limits; human analysis not presumed inherently more accurate |
| 110domain vsURLreputation | 7sections4–7, time/object/negative results/operational disclosure |
| 111screenshots/tools | 7sections7–10, screenshot vs actualinput/transmission, currentprivacy modes; obsolete per-service guarantees withheld |
| 112sandbox depth | 7sections9–10, HTML/network vs VM/hostprocess and execution conditions; no execution here |
| 113manual headers/content/anomalies | 7sections11/15–16/19–20 and8contents, source/direction/visibility |
| 114UA/rarity/versions | 7sections12–16, claimedidentity/frequencydenominator/normalexceptions/processcorroboration/currentreduction |
| 115UA components | 7sections12–13, Mozilla/platform/rv/Gecko/product/multiplecompatibilitytokens/Win64-WOW64/fixedGeckodate/currentUA-CH; no oldversion as latest |
| 116cookies/historical cases | 7sections17–19, Set-CookievsCookie/conditionalreturn/fieldlogging and ChChes/JPCERT encryption layers; M.E.Doc/ESETnormalupdateabuse and serverforensiclimitation |
| 117Base64 need/alphabet | 8sections2–3, encodingvscompressionvsencryption/64datavaluesvs=padding/legacyASCIIvsmodernapplications |
| 118conversion | 8sections4–10, originalAB bits/zero-padding/formula/changedlengths/Base64url/percent/formplus/strictfailures; no copiedAZdiagram |
| 119compound clues/encodedC2 examples | 8sections10–11/24, independentcookie/UA/hostcontext/actualdecodevsinterpretation; ATT&CKstandardencoding not attribution; no hostilepayloads |
| 120filedelivery/sharedhosting | 8sections12–18, filevsservice reputation/receivedbytesvsactualexecution/limitedvisibility |
| 121fileexport | 8sections13–18, layers/completeness/ownPCAP/checksum/hash/GUIprocedureunexecuted. OldHTTP2exportunsupportedclaim corrected against4.6.9 source. Linux alone not universal safeexecution boundary |
| 122frequency | 8sections19–22, ownCSVactualrequestgaps/dedup/meanvsrange/missing/jitter/baselines/slowpatterns/RITArole not executed/oldpopularitythreshold not permanentrule |
| 123bareIP/rootPOST | 8section23, literalHost/destination/DNSvisibility/proxy and normaldevice/API/rootrouting exceptions; no automaticC2verdict |

Original124–129 exploitkits/redirects/threeattackcases → next9=d2-07c;130–136TLS/decryption/certificates/JA3-JA3S-JARM/TLS1.3/ECH/summary → next10=d2-07d. Read-ahead not completed. Original137–138workbookpointer now planned11=id8;SMTPoldplanned9 now12;additional13/summary14/emailpractice15. Only unpublished numbers shifted, publishedday2old1–6 preserved.

## Current primary sources checked2026-11-06

- urlscan https://docs.urlscan.io/pages/visibility and currentscanAPI: Public/Unlisted/Private, unlistedProvisibility and IDsharing. Old /docs/visibility URL failed; officialcurrentdocumentation discovered normally, not bypassed. No scans submitted.
- VirusTotal https://docs.virustotal.com/docs/private-scanning :separatepaidprivilegedprivatepath, not standardupload; private results not usualmultipleAV/URLpartnerverdicts. No purchase/upload. Other named historical services not assigned unverified currentprivacy guarantees.
- Chromium https://www.chromium.org/updates/ua-reduction/ :Chrome101minorversionfreeze,107desktop/110Androidrollout context. Chrome https://developer.chrome.com/docs/privacy-security/user-agent-client-hints :89baseline/fields/policy-dependent omission; values not authenticated inventory.
- Mozilla https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox and /User-Agent :componentmeaning/fixeddesktopGecko20100101/compatibilitytokens/actualplatformlimits. MS https://learn.microsoft.com/en-us/windows/win32/winprog64/wow64-implementation-details :WOW64support32bit-on64bit, not UA authenticity.
- RFC6265 https://datatracker.ietf.org/doc/html/rfc6265#section-4.1.1 :cookie/Base64 application values, not allcookiespercentdecoded. RFC4648 https://datatracker.ietf.org/doc/html/rfc4648 :64alphabet/zero/padding/URLvariant/strictness, not secret encryption; not allmodernSMTP/HTTP universally7bitonly.
- JPCERT/CC https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html :2017-02-15 ChChescookie/encryptedencodedlayers/AESmodule, originalbook simpleBase64 wording qualified. ESET https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/ :2017-07-04 M.E.Docnormalupdate/cookieabuse/NotPetya context; source explicitly lacksserverforensics. Not every observedcookie implies malware.
- Wireshark https://www.wireshark.org/docs/dfref/h/http.html :request/host/user_agent/cookie documented1.0.0–4.6.9; contains/filterexamples unexecuted. https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html and https://www.wireshark.org/docs/man-pages/tshark.html :objects vs packet export/supporthelp. https://github.com/wireshark/wireshark/blob/v4.6.9/epan/dissectors/packet-http2.c :HAVE_NGHTTP2 condition, dissect_body_data useshttpextap and get_eo_by_name("http"). Not universallyunsupportedcurrentHTTP2; actualGUI/build/decryption/export not tested. 4.6.9 is checked source version, not permanent latest.
- Python3.12 https://docs.python.org/3.12/library/base64.html and https://docs.python.org/3.12/library/urllib.parse.html :validate/strictfailure/plus/URLsafe. Currentdocumentationpatch3.12.16 distinguished from actual3.12.14 runtime.
- MITRE https://attack.mitre.org/techniques/T1132/001/ :standardencodinginC2, no one-stringattribution. RITA https://github.com/activecm/rita and https://www.activecountermeasures.com/malware-of-the-day-understanding-c2-beacons-part-2-of-2/ :networkloganalysis/variableinterval/raritynormalexceptions; noRITAexecutionorclaimedscoreimplementation.

## Actual own examples and tests

scripts/build_http_analysis_lab.py creates8files: complete.pcap/missing-tail.pcap/expected-note.txt/intervals.csv/inspect_http.py/explore_encoding.py/inspect_intervals.py/README.txt. Own fixedIPv4/TCP/HTTP1.1 oneconversation, nohandshake/close/TLS, documentaddresses/.example. Onlytext Training only. plusnewline, noexecutable orcredential. Independent sourcecode included, rawsourcePDF/extractions excluded.

Actual Python3.12.14; direct defaultdpktimport first failed. Existing tmp/lab-deps/dpkt1.9.8 explicitly added toexecutionpath, then succeeded; no installation. check_day02_batch01_examples.py usesexistingPYTHONPATH for children. Actual17runs and66Base64lengthroundtrips0–65. Private report tmp/day2-http-check/actual-check.json, all8inputsunchanged. DefaultencodingtableA/AB/ABC/ABCD/fbff and strictmissingpadding/badchar/newline rejected;percentonceQUI=;unquoteplus changes+whileunquote preservesit. InlineABdecode=4142. Formulaschecked.

FullPCAP3frames: IPv4/TCPchecksumsvalid, header108/gzipbody35/HTTPtotal143; serverTCPsegments118+25 andsecondseq9119. Decoded15bytes matchesoriginal SHA256571143bbfd4e9e23772d8174a1f60be72d69923ed8b4a8c4744081059cd4203f. Missingtail2frames:body10/declared35/missing25/incomplete, no inventeddecode. Reorderedsegments andexactretransmission succeed; gap/conflictingduplicate/checksumdamage/declaredshort/unsupportedencoding error2. Fixedfixtureparser not generalTCP/HTTP/IPv6/TLS/HTTP2/3/chunk/parser.

SeparateCSV20rows/dedup1/unique19, notPCAP-derived20requests. A/Bgaps60x4,mean60/range0;Cgaps55/65/61/59,mean60/range10;D60/120/60,mean80/range60. Reverseorder/contexttextchange don'tchange results;conflictingduplicate/NaN/missingsource error2;singleeventgapmeanNone. Contextlabels not actualapproval. Allverdictsunresolved/externalactions0. No actualnetworkcapture/scanning/sitevisit/URLsubmission/authattempt/VM/originalworkbook/Wireshark/filter/GUIexport/TLSdecrypt/malware/fileexecution/API/block/message/accountchange/install/purchase. PublicdeploymentHTTPchecks are separate from educationalanalysis.

## Validation

Build34published. validate_day02_batch01.py passed36HTMLstructure/IDs/allrelativeassets+anchors/clickabledownloads/sixdaygroups/day1numbers1–26/day2numbers1–15/validnextd2-07c/32oldbodies+otherhomecontent/inlinecoderegressions. New46sections/161paragraphs/2tables/6SVG/26immediateexplainedquestions. Six400pxSVG Koreanfontbounds[], output/network-security/http-analysis-contact-sheet.png inspected; labels/direction/unitreadable. Sourceimagesprivate. Responsiveimage/internaltablecodescrollstructurespreserved. CUA refreshed browsers[]; actualbrowser/mobile untested, no workaround.

Publication/deployment/publiccontentproof pending. Keepactivebatch until verified; don'tstart9/10now. Wholecourseunfinished;automation-2active/local, cloudmigrationincomplete.


## Verified publication result2026-11-06

Publication07ab315a03e72e865739c7b2872ff45fb2bf7f95;Actions42199411382completed/success. Public52resourcesHTTP200/contentmatch (36HTML/CSS/coursejson/6SVG/8labfiles). TwoPCAPsandexpectedtext matchedrawbytes;othertextnormalizedLFmatched. Onlyafterproofprogress advancedday2display1–8/clearedactivebatch.32previousbodies/otherhomecontentpreserved. Next9/10source124–136 remainsplanned;originalworkbook/VM/browser/mobile unverified. Automation-2remainsactive/local, wholecourseunfinished.
