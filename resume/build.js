const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/resume.html');await p.waitForTimeout(2000);
await p.pdf({path:'../sites/vercel/resume/Arslan-Younas-Resume.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close()})();
