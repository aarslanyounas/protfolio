const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
let p=await b.newPage({viewport:{width:2000,height:500},deviceScaleFactor:2});await p.goto('file://'+process.cwd()+'/cover.html');await p.waitForTimeout(2500);await p.screenshot({path:'linkedin-cover.png'});await p.screenshot({path:'linkedin-cover.jpg',type:'jpeg',quality:96});
p=await b.newPage({viewport:{width:1200,height:1200},deviceScaleFactor:1});await p.goto('file://'+process.cwd()+'/profile.html');await p.waitForTimeout(1500);await p.screenshot({path:'linkedin-profile.jpg',type:'jpeg',quality:95});await p.screenshot({path:'linkedin-profile.png'});
await b.close()})();
