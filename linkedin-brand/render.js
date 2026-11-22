const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
let p=await b.newPage({viewport:{width:1584,height:396},deviceScaleFactor:2});await p.goto('file://'+process.cwd()+'/cover.html');await p.waitForTimeout(2500);await p.screenshot({path:'linkedin-cover.png'});await p.screenshot({path:'linkedin-cover.jpg',type:'jpeg',quality:92});
p=await b.newPage({viewport:{width:400,height:400},deviceScaleFactor:2});await p.goto('file://'+process.cwd()+'/profile.html');await p.waitForTimeout(1500);await p.screenshot({path:'linkedin-profile.png'});await p.screenshot({path:'linkedin-profile.jpg',type:'jpeg',quality:94});
await b.close()})();
