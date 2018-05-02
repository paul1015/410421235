# ML2018_410421235
Final report 410421235:
(a) the way how you prepare the training samples:
由題目給的𝒘(𝑘 + 1) = 𝐰(𝑘) + 𝛼(𝑡(𝑘) − 𝑎(𝑘))𝐱(𝑘) where 𝐰(𝑘) = 𝑤1(𝑘), 𝑤2(𝑘), 𝑤3(𝑘)]T, 𝐱(𝑘) = [𝐾1(𝑘),𝐾2(𝑘),𝐼(𝑘)]T, 𝑎(𝑘)=𝐰(𝑘)𝑇𝐱(k), 𝑡(𝑘) = 𝐸(𝑘)得知我們需要k1,k2,I,Emprime這三個圖來當作sample 用來訓練w ,因此我將這三個圖檔使用Image.open 在用getpixel 的方式轉變為陣列形式,再經由上述方法來訓練w.
(b) all parameters, such as MaxlterLimit,a and e, you used for the training algorithm:
用   epoch 當作 Epoch
用   maxlimit 當作 maxlterlimit
用   data[0] 當作 K1(k)
用   data[1] 當作 K2(k)
用   data[2] 當作 I(k)
用   x  當作   data
用   i 當作 k
用   x[0] 當作 K1(k)
用   x[1] 當作 K2(k)
用   x[2] 當作 I(k)
用   ak 當作 a(k)
用   e 當作 E 
用   ek 當作 e(k)
用   w 當作 w
用   a 當作 a == 0.00001
(c) the derived weight vector w:
w的訓練過程有顯示在jupyter notebook顯示
w = [0.22812437 0.64904842 0.10331737]
(d) the print image I’ decrypted from E’
轉好的圖已經儲存為 finalpicture.jpg 在資料庫中.
(e) the problem I encountered: 
在這次做這個作業時,剛開始還是有點不知道要如何下手,但在看到老師assignment 所給的指示,以及ppt 上的python範例後,大概就有一些
概念以及想法,但在實際操作的時候,由於很少接觸python這個語言,所以對於在寫程式上的時候,常常心有餘力而不足,無法讓程式碼去完成我想
要程式碼完成的工作,但在不停的google以及些許的詢問同學問題之後,逐漸地了解python這個語言的語法走向,以及它背後的強大功能,因此就
這樣拼拼湊湊湊合出了程式碼.
(f) what you have learned from this work:
在這次寫作業的過程中,我學到了自學能力的重要性,以及在對於virtual code 轉換到實際程式碼上面的一些技巧,想法,當然還有最重要的就
是如何使用課堂上所學的東西應用在實際的問題,以及GitHub的使用方法,可以說是相當有趣的一次作業.
