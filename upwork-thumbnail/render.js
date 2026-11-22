const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:1200},deviceScaleFactor:1});
await p.goto('file://'+process.cwd()+'/thumb.html');await p.waitForTimeout(2500);await p.screenshot({path:'upwork-thumbnail.png'});await p.screenshot({path:'upwork-thumbnail.jpg',type:'jpeg',quality:92});await b.close()})();
