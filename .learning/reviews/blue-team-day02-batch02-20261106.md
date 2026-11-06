# Day 2 batch 02: displayed lessons 9–10 — 2026-11-06

## Authorization and baseline

Direct publication of two sequential lessons per execution is authorized. Baseline main9a73cf1781a3ef1629db618c8dd4958f12a6dde0; connected account dfirwiz. Resume recorded progression, do not restart day1 or revise published lessons. First day26 and second day1–8 already published. Current IDs d2-07c/d2-07d keep displayed9/10. Next numericID8 is displayed11. Day2plan15 unchanged. No other course content or automation settings changed. Cloud migration remains incomplete/local; no claim of execution while PC/app off.

## Actual source access and role

Designated volume2 D:/SANS/SEC450/450_2022 (02).pdf physically reopened with pypdf: printed124–136, physicalPDF126–138, all13pages including separate reread132–136 after initial output truncation. Text extraction remains private under tmp/day2-http-source; no raw source or screenshots published. Printed125/PDF127 and printed131/PDF133 rendered privately with Poppler and visually inspected: exploit traffic and two-session proxy structure. Poppler reported missing display fonts Symbol/ArialUnicode; readable material cross-checked against extracted text, no claim of exact font reproduction. Other four designated PDFs remain source inventory, not falsely claimed reread thisbatch. SOURCE-MATERIALS.md and current editorial/progress/prior reviews consulted. Accessible designated folder contains five volumes and known duplicates/volume1docx. Prior scoped searches and records did not yield a separately accessible workbook/wiki/VM/original incident PCAP. This is an access limit, not a whole-system absence claim. Main textbook sets conceptual scope; original workbook execution remains unverified. Own JSON examples are separate fictional exercises.

## Source-to-lesson correspondence

| Original printed range | Concept and correction | Independent lecture location |
| --- | --- | --- |
|124|Exploit-kit purpose, compromised browsing/advertising, profile→attempt→delivery|9§2–4; attack-stagesSVG|
|125–126|Multiple hosts, obfuscation, RIG historical example, IDS, decline/cryptomining, old plugin advice|9§5–8,§20; historical2018 scope, FlashEOL correction; no reuse of original traffic or infection-success shorthand|
|127|Inbound server/honeypot Log4j example; input→lookup→download/execute implications|9§12–15; server-stagesSVG; Apache Core/API and initialfix/followups; original payload/commands not copied or executed|
|128|Outbound file-delivery redirect, dynamicDNS, multiple hosts, unfamiliarpath, archive|9§7–11,§16–17; fictionalURL comparison/bytecount calculations, delivery distinctfromexecution|
|129|jquery-likepath, repeated cookie/profile traffic, BEACON|9§18–20; library.js fictionalexample; approved tooluse/profilevariation/no single-pattern attribution|
|130|HTTPS/TLS encryption, beneficialprotection and visibility limits, DoH, validcerts|10§1–4,§7–11,§19–20|
|131|Interception organization trust, twoTLSsessions, logging/inspection|10§14–18; proxySVG; actual trust/verification/pinning/exceptions boundaries|
|132|IP/ASN/geo/ports/volume/certificate hints|10§5–10,§14,§19; TLS1.3certencrypted, names/proxy/capturecondition limits|
|133|CN,issuer,organization/selfsigned labels|10§11–14; RFC9525SAN, optionalorganization, self-issued≠cryptographically verified self-signed|
|134|JA3/JA3S/JARM, selectedfields/hash, toolclaims|10§21–27; fictionalfieldlists, GREASE/order/MD5; samevalue≠identity; JARMactivevs passive; Zeekpackageconfiguration|
|135|TLS1.3cert/SNI/ECH/privatekeys/forwardsecrecy/proxyclaim|10§5–10,§15–18; currentRFC9846/9849, PSK/0RTTexceptions, no blanket mandatorydecrypt/allprivatekeydecryptclaim|
|136|Methodical HTTP/HTTPSanalysis summary|9§21 and10§28; observation/hypothesis/missingdata with endpoint/server/firewall/resolver/proxylogs|

Original137–138 exercise pointer is NEXT displayed11, not marked completed. Original139+ SMTP scope follows; split unpublished ranges if depth requires. No unassigned conceptual items identified within124–136; this is conceptual coverage, not completion of inaccessible original workbook.

## Primary-source checks and temporal corrections

Checked 2026-11-06. Historical observations remain dated, not generalized to current incidence. Links also in relevant lecture paragraphs.

- MITRE T1189 https://attack.mitre.org/techniques/T1189/ — drive-by/normal browsing compromise concept; not proof of successful visit execution.
- Zscaler2018-08-07 https://www.zscaler.com/blogs/security-research/exploit-kits-go-cryptomining-summer-2018-edition — period-specific exploit-kit/cryptomining research; not2026prevalence.
- Adobe https://www.adobe.com/products/flashplayer/end-of-life.html — support end2020-12-31/contentblocked2021-01-12; no currentFlashinstallationrecommendation.
- Apache https://logging.apache.org/security.html and https://logging.apache.org/log4j/2.x/versioning.html — Core/API applicability,44228/45046initialfixincompleteness/currentmaintenance; 2.15.0 is historical Java8-line initialfix, never permanent latestsafeclaim.
- RFC9110 https://www.rfc-editor.org/rfc/rfc9110.html#name-location — Location/relative reference,307/308preservemethod; URL calculation not actual navigation proof.
- Mandiant2021 https://cloud.google.com/blog/topics/threat-intelligence/defining-cobalt-strike-components/ — BEACON/components and legitimate tool context; configurable profile examples not immutable detection identity.
- TLS1.3 CURRENT RFC9846 https://www.rfc-editor.org/info/rfc9846/ and https://www.rfc-editor.org/rfc/rfc9846.txt — July2026, obsoletesRFC8446 but stillTLS1.3. The htmlendpoint failed; working info/txt sources actually read. legacy_version0303 vs actualselection0304; encryptedpostServerHello; PSK-only/0RTTexceptions. This materially updates old standardreference without inventingTLS1.4.
- ECH RFC9849 https://www.rfc-editor.org/rfc/rfc9849.html — March2026publishedstandard, not merelyfuture draft; Inner/Outer/SNI/ALPN, observableotherchannels, GREASEECH presence not acceptancesuccess.
- RFC9525 https://www.rfc-editor.org/rfc/rfc9525.html — Nov2023replaces6125; DNS-ID SANdNSName notCNserviceidentity. RFC5280 https://www.rfc-editor.org/rfc/rfc5280.html — certificate/path/selfissuedvs selfsigned.
- Let'sEncrypt https://letsencrypt.org/how-it-works/ — domaincontrolvalidation notcontentsafety.
- PaloAlto official https://docs.paloaltonetworks.com/network-security/decryption/administration/decryption-overview/ssl-forward-proxy — twoTLSsessions, pinning/clientauth/decryptionexceptions; notallproducts/modesguarantee.
- Wireshark https://wiki.wireshark.org/TLS — keylogs vs restrictedRSAprivatekeyconditions; noactualdecrypt. https://www.wireshark.org/docs/dfref/t/tls.html — displayedfieldreferences3.0.0–4.6.9 checked, notcurrentinstalledversionclaim/permanentlatest. Filters unexecuted; multimessageframe association/capture limits explicit.
- Salesforce https://github.com/salesforce/ja3 — fields/order/GREASE/JA3S, archivedMay1 2025andnotactivelymaintainedbySalesforce. https://github.com/salesforce/jarm — active10ClientHelloprobes, no probes executed.
- Zeekofficialpackage https://packages.zeek.org/packages/view/cebd1c8c-9348-11eb-81e7-0a598146b5c6 — package/load/support notuniversalcoredefault.
- RFC8701 https://www.rfc-editor.org/rfc/rfc8701.html — reservedGREASEvalues. Python https://docs.python.org/3.12/library/hashlib.html — MD5legacyusedforsecurityFalse; actualruntime3.12.14 distinguished from current3.12documentationpatch3.12.16.

## Actually executed examples and limits

Five downloadable text files: cases.json/review_chain.py/hello-fields.json/fingerprint_hello.py/README.txt, only standardlibrary localread/computation/output. No networkrequests, originalcommands, packageinstallation, cert/keycollection, workstationconfiguration, TLS negotiation, realpacketextraction, JARMprobe, malwareexecution or originalworkbook completed. Fictional documentIP/.exampledomains only.

check_day02_batch02_examples.py executed22 condition/invalid-input runs. Original five downloadable files SHA256 unchanged. R1no successor, R2exact URL match, R3differenthost;307relative and absoluteLocationhostchange; equalURLstillcausalityfalse. F1metadata35/35,F2missing25,F3reportedclaimnotrealverification. Malformedcredential/nonHTTP/booleanstatus/badexecution/negative/excess/nonintegercounts rejected. H1/H2/H4sameMD5 e2cffc125debe8b8da45016372134155; H3orderchange be3d7e78f53aa58ea985052d91ab501a. All16GREASEreservedvalues added in3relevantlists ignored asdesigned; labelsdon'tchangefeatures. Booleanversion/outofrangegroups/pointformats/nonintegercipher/emptyrecords/unauthorizedcontract rejected exit2. Every successful recordexternal_actions0/unresolved; no packet/TLS/identity/causality verification invented. URL comparison deliberately not canonicalization/session/time/tabs/causality or full redirect implementation; HelloJSON deliberately not realwiremessage validation. Actualcheck report tmp/day2-tls-check/actual-check.json.

## Build and validation

Final build and static validation rerun passed after prose/first-use-term/caption corrections. Builder scripts/build_network_security.py includes new diagram helper and clickable day02-lab10 downloads. Static validator checks38HTML,36published,34previousbodies preserved, otherhomepage content unchanged, daygroups/numbering/links/anchors/HTMLnesting/code/download regressions. New9=22sections77paragraphs3SVG14Q&A;10=29sections102paragraphs3SVG2tables16Q&A (paragraphs may remain same after corrections). All30answers immediately visible. SixoriginalSVG400px wide/fontbounds[] and contact sheet visually inspected; captions/directions/legends matched. Table/code internal overflowCSS preserved. Browser inventory freshly checked: browsers[], therefore actualbrowser/mobile rendering unavailable, not bypassed. Static Koreanfont rendering is not browserverification. Popplerprivate rendering warnings disclosed above.

## Publication gate

Content validated locally; remote commit/Actions/public verification pending. Completedday2 stays1–8 until deployment success AND public51resourceHTTP200/contentmatch. If failure preserve this batch and resume, never rewrite completed lessons. After successful publication next displayed11 starts original137–138exercise, then nextunpublished SMTP material. Entirecourse unfinished, automation active/local.


## Verified publication result2026-11-06

Publication175fbc6d9a81e329da70b14bac15e9a3f0987c19;Actions42207005049completed/success. Public51resourcesHTTP200/contentmatch (38HTML/CSS/coursejson/6SVG/5textlabfiles). Onlyafterproofprogressadvancedday2display1–10/clearedactivebatch.34previousbodies/otherhomepagecontentpreserved;51sections179paragraphs2tables6SVG30immediateQ&A. Next11original137–138exercisepointer,thenSMTP139+ selectedandsplitasneeded. Originalworkbook/VM/browser/mobileunverified;automationactive/local,wholecourseunfinished.
