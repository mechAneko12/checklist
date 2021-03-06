
## <span style = "color: Deepskyblue"> Deep Image Prior(2018)</span>

> #  ***概要*** <br>
>   <span style = "color: Aqua; ">CNN</span>を用いて、
その特性によって画像データのデノイズや補完を行う手法についての論文です。画像の圧縮などによって生じた不明な劣化を修正することができ、自然な画像については最適化が速く進み、自然でない（シャッフルされたもの、ノイズ）については不活性な性質を持つことが検証されています。<br>
>   　画像の劣化課程を知ったり事前学習したりする必要なく補完できる。
> - **CNN** <br>
>   ネットワークは、1)<span style = "color: Yellowgreen; ">ダウンサンプリング</span>, 2)<span style = "color: Gold; ">スキップコネクション</span>, 3)<span style = "color: red; ">アップサンプリング</span>の3種類のモジュールから成り立っており(Fig 1)、ランダムな画像データを入力、ランダムな値を各層の重みとしています。最適化に平均二乗誤差を用いています。。超解像の際には、出力をダウンサンプリングしてから元画像と誤差関数で比較します。また、インペイントをする場合、バイナリマスクと差分との要素積をとってから誤差関数に入力する。これにより書き込みのない部分だけで評価しています。
>   ###### <div align="center"><img src="img/Fig1.png" width=700><br clear="left">Figure 1: Deep Image Prior アーキテクチャの構造
> </div><br>
>
> - **実験結果の概要**
>   - 超解像について、バイキュービック法と比較すると明らかに高解像度化に成功していることがわかった(Fig 2)。
>   ###### <div align="center"><img src="img/Fig2.png" width=700><br clear="left">Figure 2: バイキュービック法, Deep Image Priorの超解像の比較
>   </div><br>
>
>   - インペインティングについては、テキストを挿入した画像、ベルヌーイ分布によるマスクをした画像、白い巨大な抜け落ちのある画像を基にほかの手法との比較を行い、いずれも高い再現性を示している。
>   - "natural pre-image"という、ネットワークを反転させて出力する値を指標とすることで、ネットワークがどのようなアクティベーションをしているのかという情報を理解する手法がある。これによってL1正則化を取り入れたTV norm prior、学習済みのネットワーク、Deep Image Priorの3つを比較し、Deep Image Priorの優位性を示した。
>   ###### <div align="center"><img src="img/Fig3.png" width=700><br clear="left">Figure 3:AlexNetの各層を反転して、Deep Image Prior, TV prior, 学習済みの反転ネットワークのnatural pre-imageの比較
>   </div><br>
>
>   - フラッシュ撮影した画像をガイドとして、フラッシュを使わない画像の復元にも成功している。
> 
> 　
> <br>

> #  ***疑問点のリスト*** <br>
>   - 畳み込みの性質によって線などの構造をとらえ、自然な画像が構成できることは感覚的にはわかるのですが、理論がよくわかりません。
>   - "natural pre-image"の仕組みがよくわからない。（画像をAlexNetに入力し、AlexNet各層の値をそれぞれのreguralizerに入れてさかのぼるような向きにネットワークを通して、出力する？）

> # ***論文に対する批判・改善案***　<br>
>   - 完全なランダムの画像データから元の画像に近づけていますが、残しておきたい部分のエッジなどを乗せたら~~さらに高画質になる、もしくは~~少ない学習や変数・層での補完ができるのではないかと考えました。
>   - 一般的な誤算関数の平均二乗誤差を用いていますが、どうしてそれを使っているのか根拠が少し気になりました（ほかの関数との比較などをした結果なのかどうか）。 

> # ***実装*** <br>
> - pytorchで各モジュール5つ分のネットワークを作って、デノイズ、超解像、インペインティングを行いました。
>   |original image| gaussian noise | denoise |
>   |:---:|:---:|:---:|
>   | <img src="img/yeji_0.jpg" height=400>| <img src="img/yeji_noise.jpg" height=400>| <img src="img/yeji_noise_prior.jpg" height=400> |
>
>   |original image| smoothing | super resolution |
>   |:---:|:---:|:---:|
>   | <img src="img/yeji_0.jpg" height=400>| <img src="img/yeji_mosaic0.jpg" height=400>| <img src="img/yeji_mosaic0_prior.jpg" height=400> |
>
>   |original image| painted | inpainting |
>   |:---:|:---:|:---:|
>   | <img src="img/yeji_0.jpg" height=400>| <img src="img/yeji_inpaint.jpg" height=400>| <img src="img/yeji_inpaint_prior.jpg" height=400> |
>
> - 失敗
>   |original image| gaussian noise | denoise |
>   |:---:|:---:|:---:|
>   | <img src="img/yeji_0.jpg" height=400>| <img src="img/yeji_noise0.jpg" height=400>| <img src="img/yeji_noise0_prior.jpg" height=400> |
>   |||変数の変化が小さく、<br>Redが少なくなって<br>しまっている|
>
>   |original image| painted | inpainting |
>   |:---:|:---:|:---:|
>   | <img src="img/yeji_0.jpg" height=400>| <img src="img/yeji_inpaint0.jpg" height=400>| <img src="img/yeji_inpaint0_prior.jpg" height=400> |
>   |||ネットワークの最後が<br>leakyReLUだったので、<br>白く飛んでいる|
