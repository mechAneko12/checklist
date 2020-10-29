## 混同行列

<table>
<tr>
<th colspan="2" rowspan="2" bgcolor=#c2c2c2></th>
<th scope="col" colspan="2" bgcolor=#c2c2c2><font color="Black">予測した値</font></th>
</tr>
<tr>
<th scope="col" bgcolor=#c2c2c2><font color="Black">Positive</font></th>
<th scope="col" bgcolor=#c2c2c2><font color="Black">Negetive</font></th>
</tr>
<tr>
<th rowspan="2" bgcolor=#c2c2c2><font color="Black">実際のクラス</font></th>
<th scope="col" bgcolor=#c2c2c2><font color="Black">True</font></th>
<td align="center" scope="col" bgcolor=#db4442>TP</td>
<td align="center" scope="col" bgcolor=#43c1f7>TN</td>
</tr>
<tr>
<th scope="col" bgcolor=#c2c2c2><font color="Black">False</font></th>
<td align="center" scope="col" bgcolor=#43c1f7>FP</td>
<td align="center" scope="col" bgcolor=#db4442>FN</td>
</tr>
</table>

> **混同行列**とは、上のような表によって分類問題の結果を示したものである。分類する対象によって、予測した結果によって利益・不利益が大きく変動するので、混同行列によりどのように誤って予測しているのかを知るのかを知る必要がある。
> その評価指標として、**Precision, Recall, F値, IoU**がある。
> - **Precision**
>   $$Precision=\frac{TP}{TP+FP}$$
>   Positiveを確認する指標として使われている。誤検知に対する強さを測ることが目的。
>   <br><br>
> - **Recall**
>   $$Recall=\frac{TP}{TP+FN}$$
>   Trueの見逃しに対する強さの指標。
>   <br><br>
> - **F値**
>   $$F=\frac{TP}{TP+\frac{1}{2}(FP+FN)}$$
>   PrecisionとRecallの調和平均をとり、誤検知と見逃しに対する強さの指標とされている。
>   <br><br>
> - **IoU**
>   $$IoU=\frac{TP}{TP+FP+FN}$$
>   予測がどのくらいうまく真値を包括しているかをはかる値。