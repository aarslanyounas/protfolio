const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:627},deviceScaleFactor:2});
await p.goto('file://'+process.cwd()+'/linkedin.html');await p.waitForTimeout(2500);
await p.screenshot({path:'linkedin-featured.png'});await p.screenshot({path:'linkedin-featured.jpg',type:'jpeg',quality:90});await b.close()})();
