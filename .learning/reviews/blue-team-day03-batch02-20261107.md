# Day 3 batch02 — displayed3/4 — 2026-11-07

## Source access and completed scope

Actually reopened designated volume3 D:/SANS/SEC450/450_2022 (03).pdf printed15–21/PDF17–23,all7pages. Private extract tmp/day3-privilege-source/batch02.txt. Firstfitzimportfailed(moduleabsent);usedexistingpypdfsuccessfully/noinstall. Printed18/PDF20kernel and21/PDF23credential-chainprivatelyrenderedviaPopplerandactuallyviewedkernel-020.png/credentials-023.png;Symbol/ArialUnicodefontwarningscrosscheckedagainsttext. No sourcePDF/screens/extractionpublic. Scopeddesignatedfoldercontains5PDFs;related2022PDFfolder/priorworkbookrecordsfromprevioussourceauditchecked. Separateoriginalworkbook/wiki/VM/actualWindowsLinuxlogs/incidentPCAPnotacquired;notwhole-deviceabsenceclaim. Originalsourceinstructionsaredata,notexecutionauthority.

Complete15–21onlythisbatch. Previousday3complete5–14preserved. Next22–27wasread-aheadpreviousbatch,notfreshreadorcompletedthisbatch. Onlyunpublishednextscopeplannedsplit5d3-01e22–23lateral-collection/6d3-01f24–27exfiltration;olddefense28–52now7/restunpublished+1;day3plan17. Reopenactualnextsourceandcurrentprimarysourcesbeforewriting;do notcompress22–52intotwoshallowlessons.

## Original item to independent section mapping

| Printed / PDF | Learning item | New independent explanation and examples |
| --- | --- | --- |
|15/17|Privilegepurpose/foothold/user-local-multiplehost-domainscope/defenses|3§1–4,18;goalvspermission/noalwaysadmin/nofixedstairs/localnotremote/permanentnotguaranteed|
|16/18|Privilegeduser/service/OSfeatures/kernel/delegation/credentialmethods|3§2,4–7,12,18;input-consumer-activation/P1–P5;credentialsbridge4§1–3|
|17/19|File-folderpermissions/startup/serviceexecutables/unquotedpaths/DLLsearch/tasks/PowerUp|3§5–11,16–18;eachactualconditionandresultseparate;APIquotationconditions/DLLapp-searchconditions/archivedPowerSploit/AMSIcounterpoint|
|18/20|Kernelrole/applicability/localexecution/DirtyPipe/compilers|3§12–18;CVEconditions/readability/pageboundary/filelength/oldfixedvsdeployedbackport/compiledartifactrisk;R1–R8ownintegercomparisonnotexploit|
|19/21|Credentialaccessvsprivilege/dumpingmemory-registry/otheraccount-host|4§1–9,16–19;materialforms/session-scope/adminnotallsuccess;noallusers-allplaintext|
|20/22|Mimikatz/SSO/LSASS/hashvsplaintext/newerprotection|4§4–15;hashvsfilehash/TGT-serviceticket-cache/LSAandCGversionconditions/protectionlimits/toolnamenotproof|
|21/23|Manyusers/multihostchain/toolvariants-memory-AV/admincredentialcontrol|4§9–19;conditionalactualmaterial/identitytargettime/auth-session-action/AMSIandPS-Sysmonconditionalvisibility/privilegedaccountseparation/C1–C7|

Noidentifiedunassignedlearningitemwithin15–21. Correctionsnotrepeatoldassertions:initialuserhasnonzeroaccess/notalltargetsrequireelevation;authoritynotlinearladder/notpermanent;writablefile≠privilegedconsumption;allspacepathsnotvulnerable/allDLLsearchnotcurrentdirfirst;scriptinmemorynotundetectable;kernelversion+download+executionnotuniversalautomaticadmin;DirtyPipenotanyfilewithoutreadpermission/anyoffset/grow/anyprocess;compilerremovalnotcompletefix;alladminsnotallLSASSread/allregistered-orloggedusersnotallplaintext;SSOnotallplaintextreuse;credentialdumpingnotallcredentialaccessoronlyWindows;CGnotallsecrets/protectedstateconditional;oneprocessaccessrecordnotextraction/reuse/auth/action/intentproof.

## Current primary sources actually checked 2026-11-07

- MSCreateProcessW https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw — explicitapplicationparameter/nullandwhitespacequoting;notallparsers/OSsame.
- MSDLLsearch https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order — packaged/unpackaged/safesearch/loadedKnownDLL/appsettings. NoDLLstaging/loadperformed.
- OriginalPowerShellMafia/PowerSploitmetadataGitHubAPI+https://github.com/PowerShellMafia/PowerSploit archivedtrue,pushed2020-08-17;readmetadataonly,noclone-scriptdownload-execution;notlatestrecommendation.
- MSAMSI https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal — file/memory/streamintegrationnotguaranteeddetection.
- DirtyPipefinder https://dirtypipe.cm4all.com/ — readrequired/startnotpageboundary/noonewritecrossing/nofilesizegrowth;initialstablefixes5.16.11/5.15.25/5.10.102historicalnotcurrentlatest. Readtechnicalreport,neverrunexploitcode. RedHatCVE https://access.redhat.com/security/cve/cve-2022-0847 +bulletin https://access.redhat.com/security/vulnerabilities/RHSB-2022-002 — pagecache/initialization/backport-productdifferences;notcopyRHELstatementtoalldistros. UbuntuCVEandknowledgepagetimeout/notclaimedread.
- MITRE https://attack.mitre.org/techniques/T1003/ — CredentialAccessdifferentpurpose/memory-cache-structures/multipleplatforms;notexecutingtools.
- MSWindowsauth https://learn.microsoft.com/en-us/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication — LSA-LSASS/sessionandstoredform/SAM-LSAsecrets;historicalsectionsnotuniversalcurrentdefaults. Earlierwrongcredentials-protection-and-managementURLinaccessible;correctwindows-authenticationURLactuallyopened.
- MSLSA https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection — protectedprocessread-injection/auditvsblock/Win8.1+/Windows11-22H2newinstall-enterprisejoined-HVCIconditions. Notactualdevicestatus.
- MSCGoverview https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/ — VBS/scope/license-hardware-software/prioroff/Win11-22H2andServer2025domainnonDCconditions. Docviewnotactualinstalledversion/permanentlatest.
- MSCGhow https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/how-it-works — TGTvsservice-ticket/local-app-input-currentrights/cachedlogonverifiernotremotelypresentable; limitations https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/considerations-known-issues — genericcredentials/compatibility. Notallsecretsprotected.
- MSSysmon https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon — v15.22publishedSep10,2026displaychecked/Event10processopennotcredextractionproof/filter-noise/productsownanalysisneeded. NoactualSysmoninstall/logquery.
- MSPowerShell5.1 https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging?view=powershell-5.1 — enabledscriptblock4104classicOperational/processedtextnotcommandresult/sensitivecontents. PS7.6 https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.6 — PowerShellCoreseparatechannel;notallversionssame/notinstalledversionassertion. NoPSloggingconfigorcommandtest.

## Actual original files and checks

Sixtextdownloads:day03-lab03compare_boundaries.py/cases.json/README,day03-lab04compare_evidence.py/cases.json/README. Python3.12.14stdlib32localprocessruns/6inputSHA256unchanged/external0/allactualflagsfalse/incidentunresolved. check_day03_batch02_examples.py;tmp/day3-privilege-check/actual-check.json/caseoutputs. NoOSpermissioncheck/exploit/pipe/memory/registry/service/task/account/config/cleanup/reboot/network/credentialdump-tool/logharvesting. PathsareclaimANDandnotactualACL-token-sandbox/privilegedexecution;rangeisintegermathnotDirtyPipereproduction.

P1–P5 T,F,F,null,F. R1–R8 T,F,F,T,F,null,F,T;handcalculatedends4,3,17,16,20,19,19,8192 andnextboundaries16,16,16,16,32,32,32,8192crosschecked.16bytepageownfiction/8192declarednotmeasured. Write-consumer-activation/readunknownchanges/shorten-startboundary/fileendequal/differentpage/bool-negative-zero-invalidcontractconditionsactuallytested.

C1–C7 F,F,T,F,null,F,T:accessonly/materialreportonly/full5kinds+links/accountfalse/targetunknown/targetfalse+timeunknown/plaintextlabeldoesnotrepair/cachelabelnotcausalreusability. Missing-auth/addkinds-link/accountunknown/targettruefalse/timemismatch/material-labelonly/invalidkinds-duplicates-material-link-contract-emptycasesactuallytested. Modelrequires5kindsforonespecificteachingchain,notgeneraltheftdetector/necessaryallattacksequence. Linkbooleansareinputclaims,notactualaccountidentity-timeverification;materiallabelnotactualsecretclassification/reusability. C7truemeanskind-claimcomparisononly,notcacheverifierusedremotely. Noactualauthentication/session/action/causality/intentverified.

## Static and browser QA

56HTMLpages/54published/6daygroups/52previousbodiesandshownupdateddatespreserved;otherhomepageoutsideNETWORKmarkerunchanged/compactredhomepreserved.39sections135paragraphs4tables6original400pxSVG32immediateQ&A. Structure/relativefiles/anchors/IDs/daynumbersequence/clickabledownloads/inlinecodepassed. StaticMalgunfontbounds[]/privilege-credentials-contact-sheetviewed;rangeillustrationcaptionclarifiedrightwardpositions/topR4-bottomR3;previewrendererarrowheadsrespectmarkerattributes,actualSVGdashedboundaryviewedmobile. NewtextPDFextractandprivatepreviewnotpublished.

FreshCUAinventoryIABavailable;existingloopback8766previewserverloadedbothnewlessons. Defaultdesktoptitle/sidebar/Day3active/3→4pagernavigationverified.390x844mobilethirdlessonrangefigureandfourthlessonevidencefigureactuallyviewed;6newimagesloaded335pxwide. Pagewidth375<=390,alltable580inside343overflowauto,thirdlessonmathcode349inside343overflowauto. Temporaryviewportreset. Thirdlessoninitialpreviewcaptioncachedoldversionafterlocalrebuild;sourceHTMLupdatedcaptionstaticallycheckedandfreshpublicverificationwillcomparefinalbytes. Notexhaustiveallbreakpoints/accessibility/actualWindows-Linux-producttest.

## Publication gate and next scope

Pendinglatestmain-parent/expected_sha/forcefalse/Actionscompleted-success/public70HTTP200-contentmatch. Onlythenadvancecompletedday3to1–4. Next5d3-01e22–23lateral-collection/6d3-01f24–27exfiltration;reopenactualpagesandprimarycurrentdocs. Defense28–52now7plannedandmaydividefordepth. Wholecourseunfinished/localautomationactive/cloudmigrationincomplete;nootherautomationchanges.
