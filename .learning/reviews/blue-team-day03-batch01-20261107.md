# Day 3 batch 01 — displayed 1/2 — 2026-11-07

## Source access and scope

Designated volume3 D:/SANS/SEC450/450_2022 (03).pdf,173physicalPDFpages. Printed5–27/PDF7–29actuallyread this batch;25–27reread separately after combined output truncation. Private extract tmp/day3-tactics-source/batch01-read-ahead.txt. Printed8/PDF10 and12/PDF14privatelyrendered/viewed initial-context-010.png/execution-014.png;Poppler font warnings crosschecked against text. Complete only printed5–14/PDF7–16,15–27read-ahead not completion. No sourcePDF/screens/extraction published. Scoped designatedfivePDFs/related2022PDFfolder/priorworkbookrecords checked;separateoriginalworkbook/wiki/VM/actualendpointlogs/incidentPCAPnotacquired. Not claim of whole-device absence. Independent own comparison practice,not completion of original workbook or real endpoint validation. Document instructions are learning data only.

## Source item to independent section mapping

| Printed / PDF | Learning item | Independent lecture coverage |
| --- | --- | --- |
|5/7|Roadmap and viewpoint transition|1§1–4;2§1;lateritems15–27explicitlydeferred|
|6/8|Endpoint process/user/inside-tunnel vantage;attack-flow categories|1§1–2,5–9,16;conditionalvisibility,notautomaticallycomplete|
|7/9|Network delivery to endpoint stages;learningassumedsuccess|1§1–4,16;assumptionseparatefromproof/nonlinearstages|
|8/10|Initial exploit/socialengineering/context/user-admin-service|1§3,5–9,13–15;E1–E6;lowprivnonzeroimpact/UAC/context/remoteboundary|
|9/11|Service-side path/reachability/repeatedattempts/firewallpatch|1§10,12,16;rolesnotdevicetype/openportnotproof/conditionsnotuniversal|
|10/12|Client-side document/browser/userinteraction/reaccess|1§11–12,16;previewconditional/notallclick/notallcallback/repeatabilitynotabsolute|
|11/13|ATT&CK tactics/purposes|2§1–3;currentv20.1/15tactics/StealthTA0005andDefenseImpairmentTA0112;notonlypostexploit/notfixedsequence|
|12/14|Execution/shell/controltools/builtins/PowerShell/SQLxp_cmdshell/applicationcontrol|2§4–6;feature-role-proxy-servicecontext/audit-enforce-log-alertdifferent;toolsnotexecuted|
|13/15|Persistenceoptional/reaccess/Run/task/partialcleanup|2§7–10,13–17;logonnotboot/tasktrigger-action-principal/configvsactivation/alternativepaths/T1–T6|
|14/16|Discoveryaccounts/groups/rights/files/processes/services/hosts/apps/LOTL|2§11–12,13–17;baselinecontext/outputnotassumed/observedcommandnotintent/secretproof|

No identified unassigned learning items within5–14. Original text assertions corrected rather than reproduced:limitedserviceisnotnothing;adminmembershipnotactualelevation;localnotremote;exploit≠allinitialaccess;server/clientrolesnotexclusivehardware;openport/outdatedversionnotexploitsuccess;manualclick/callback/repeatabilitynotuniversal;initialaccessnotautomaticOSshell;SQLloginnotOSadmin/xp_cmdshelldisableddefault/rightsproxyconditions;AppControlauditnotnecessarilyblock/lognotinstantSOC;Runlogonnotallboot;taskregistrationnotexecution/notallSYSTEM;onefiledeletionnotallpathsremoved;builtinsnotautomaticallynormalorundetectable.

## Current primary sources checked 2026-11-07

- Microsoft access control: https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/access-control — principals/ACL/requestedaccess/authentication-authorization;displayedOSdocscopeisnotactualdeployment/supportrecommendation.
- Microsoft UAC: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works — interactiveAdminApprovalfiltered/elevatedtokens;notallserviceorOScontexts.
- Linuxman-pages capabilities: https://man7.org/linux/man-pages/man7/capabilities.7.html — UID0traditional/capabilitiesLinux2.2+;notWindowsadminequivalence.
- MITRE versions: https://attack.mitre.org/resources/versions/ — currentv20.1since2026-10-13; https://attack.mitre.org/versions/v20/ preserved; https://attack.mitre.org/tactics/enterprise/ 15tactics; https://attack.mitre.org/tactics/TA0005/ Stealth / https://attack.mitre.org/tactics/TA0112/ DefenseImpairment. Currentnamesverified,notclaimexactrelease-splitcausality;classificationnotproof/onlypostexploitation.
- Microsoft SQL Server: https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-ver17 — defaultdisabled/callerrights/serviceorproxycontext;viewnotactualinstalledversion/permanentlatest.
- AppControl https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/select-types-of-rules-to-create — audit/enforce/optionsconditional;recordingnotalertguarantee.
- Run/RunOnce https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys — logon/conditions.
- Tasks https://learn.microsoft.com/en-us/windows/win32/taskschd/task-triggers / https://learn.microsoft.com/en-us/windows/win32/taskschd/security-contexts-for-running-tasks — trigger/action/principal/credentials/rights.
- ASD official2024jointLOTLadvisory https://www.cyber.gov.au/advisory/identifying-and-mitigating-living-off-the-land-techniques — behavioralcontext/baseline/logging. FullFBIlinkedPDFtimedout/notclaimedread;HTMLadvisorychecked. Historicalpublicationdatenot2026incident/currentproductclaim.

## Actual independent runs and limitations

Sixowntextdownloads:lab01compare_context.py/cases.json/README,lab02compare_activity.py/cases.json/README. Python3.12.14stdlib32localprocessruns;6inputSHA256unchanged;externalactions0/allincidentunresolved/allactualverificationflagsfalse. Private tmp/day3-start-check/actual-check.json and case outputs;check_day03_batch01_examples.py.

Context E1read/writeuserdata/internalconnectiontrue/changeconfigfalse;E2adminmemberclaimtruebutchangeconfigfalse;E3servicedatareadtrue;E4localclaimdoesnotaddremoteaction;E5unknownnullvsE6knownemptyfalse. Group/label-onlychanges/explicitactionchange/explicitremoteclaim/requestsubset/null-emptyandinvalidcontractschecked. NotWindowsACL/token/inheritance/deny/sandbox/Linuxcapabilitysimulation/notactualpermissionsaccessorremoteauthorization.

Activity T1processonly/T2configonly/T3samehost-subjectcfg10:00→trig10:05→proc10:06onecandidate['cfg','trig','proc'];T4otherhostnone/T5discoveryclaimonly/T6othersubjectnone. Equivalenttimezone/triggerafterstart/missingtrigger-config-process/emptyrecords/alternativepath/invalidkind-naivetime-order-duplicateID-contractschecked. SubjectistoylabelnotPID/fileidentity/causalID;noactualcommands/processstart/task/registry/reboot/SQLfeatureenabling/network/configuration/cleanupperformed. Currentnewsourcerawtextnotpublic.

## Static and browser validation

54HTMLpages/52published/6daygroups;35newsections/124paragraphs/3tables/6original400pxSVG/28immediateQ&A. Structure/relativefiles/anchors/uniquecourseIDs/daynumbersequence/clickabledownloads/codeformatpassed.50priorbodycontentandshownupdateddatespreserved;compactredhomepageandotherhomecontentoutsideNETWORKmarkerunchanged. StaticMalgunfontbounds[]/endpoint-start-contact-sheetactuallyviewed. Existingimagewidth100%/table-codeinternaloverflowruleskept.

FreshCUAinventorynowprovidesIAB(previousbatchdisabledisnotcurrentfact). Initiallocalhostrefusedbecausepreviewserverstopped;startedownedloopback-onlyserverport8766hiddenandloadedbothnewpages. FirsttaberrorpagegetwasblockedbydataURLpolicy;didnotinteractwithblockeddataURL;originalallowedlocalhostnewtabloaded. Defaultdesktoptitle/sidebar/activeDay3/lesson1→2navigationverified.390x844viewportmobiletitle/text/firstfigurevisuallyinspected;read-onlyDOMpagewidth375<=viewport390,firstfigure335px,table580inside343pxoverflowauto,code354inside343pxoverflowauto. Lazyimagesnotyetvisitedarenotclaimedloaded;all6SVGstaticallyrendered/viewed. Morebrowserfindings/publicproofpending. Temporaryviewportreset. NooriginalWindows/VM/productexecutiontest.

## Publication gate

Pending connectorlatestmain/expected_sha/forcefalse;Actionscompleted-successand68publicHTTP200/contentmatchrequiredbeforeupdatingcompleted. Nextday3display3d3-01cprinted15–18/PDF17–20privilegeand4d3-01dprinted19–21/PDF21–23credentials;actuallyreopenrespectivepagesandcurrentprimaryreferencesbeforewriting.15–27onlyread-aheadthisbatch. Wholecourseunfinished/localautomationactive/cloudmigrationincomplete.


## Verified publication result 2026-11-07

Content 95a65f38ca1d2dba3f478f965a0b01974dbd31b6;Actions 42342351466 completed/success(build/deploy/reportallpassed). Public68resourcesHTTP200/contentmatch:54HTML/CSS/coursejson/6SVG/6textdownloads,LFnormalized. Nativepublicationtreea0e90ceb119466c5cc7789afb88be52a7ccd9278equalsconnectortree.75ownedcontentpaths. Onlyaftertheseproofsadvancedday3display1/2-clearedactivebatch-next3/4;day1=26/day2=24preservedand52totalpublished.35sections124paragraphs3tables6SVG28immediateQ&A. Browseradditionalfindings:FreshIABavailable. Localdefaultdesktopand390x844mobiletitle-text-firstfigureandsecondtablevisuallyinspected;pagewidth375<=390/table580inside343overflowauto/code354inside343overflowauto;all3secondlessonlazySVGloadedaftersection15navigation. All6SVGstaticMalgunfontbounds[]/contactsheetviewed. Publicsecondlessonsection9heading-body-startupSVGandactiveDay3sidebarvisuallyverified;desktoppagewidth1265<=1280. Viewportreset/completion_summarysent. Notexhaustiveeverybreakpoint/accessibilitytest.. ActualOS-permissions-token-task-command-causality-originalworkbook-VMunverified. Source5–14complete/15–27read-aheadonly;next15–18privilege/19–21credentialsreopenbeforewriting. Wholecourseunfinished/localautomationactive/cloudmigrationincomplete.
