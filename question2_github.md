# 問２

## (1) アルゴリズム

>  -  **最尤推定法**<br>
> 教師あり学習。ある確率分布<img src="https://latex.codecogs.com/gif.latex?q(x_i;\theta)">から生起する確率密度、すなわちすべてのカテゴリの確率分布の積を以下のように尤度<img src="https://latex.codecogs.com/gif.latex?L(\theta)">とする。<div align="center"><img src="https://latex.codecogs.com/gif.latex?L(\theta)=\prod_{i&space;=&space;1}^{n}q(x_i;\theta)"></div>
>  この値が最大のときに最も尤もらしい分布といえる。尤度が最大の時に偏微分の値が0になるという性質から、その時のパラメータ$\theta$を求めるための方程式は以下のようになる。これを尤度方程式という。<div align="center"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial&space;\theta}\textrm{log}L(\theta)=0"></div>
> 尤度方程式を解いて尤度を最大にするようにパラメータ<img src="https://latex.codecogs.com/gif.latex?\theta">を決定する。決定したパラメータに基づいて事後確率を求め、事後確率が最大のクラスに分類する。
>
>  -  **<img src="https://latex.codecogs.com/gif.latex?k">近傍法**<br>
> 教師あり学習。最も簡単な仕組みの機械学習の手法である。パラメータによって定義されたベクトル空間の点から（一般的に）ユークリッド距離で最も近い<img src="https://latex.codecogs.com/gif.latex?k">個の点がどのクラスに割り当てられているかを確認し、もっとの多いクラスに分類する。
>
>  - <img src="https://latex.codecogs.com/gif.latex?k">近傍法<br>
> 教師なし学習。以下の手順でクラスタに分類する。
>       1. 各点<img src="https://latex.codecogs.com/gif.latex?x_i">をランダムに<img src="https://latex.codecogs.com/gif.latex?k">個のクラスタに分類する。
>       2. 各クラスタの重心を求める。
>       3. 各点<img src="https://latex.codecogs.com/gif.latex?x_i">と各クラスタの重心の距離を求め、距離の近いクラスタに振り分ける。
>       4. 振り分けられるクラスタが変化しなくなる、または変動が閾値を下回った時に終了する。

## (2.2) **numpy 2d array X_new**

> ```python:question2.py
>  X_new = np.concatenate((np.ones((X.shape[0],1)), X), axis=1)
> ```

  

## (3.2) **ロジステック回帰**

>  - **ロジスティック回帰の関数**
>  > ```python
>  >  def  f(x, b):
>  >    return  1.0 / (1.0 + np.exp(-np.dot(x, b.T)))
>  > ```
>  - **bは正規分布で生成**<br>
> 正規分布はガウス関数$$f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}> \textrm{exp}\biggl(-\frac{(x-\mu)^2}{2\sigma ^2} \biggr)$$
> で与えられる。<img src="https://latex.codecogs.com/gif.latex?\mu">: 平均, <img src="https://latex.codecogs.com/gif.latex?\sigma^2">: 分散に従う

  

## (3.3) **他クラス分類の時のy_predの扱い**

  

> クラス<img src="https://latex.codecogs.com/gif.latex?i\in\{1,\cdots,n\}">について、$y=i,y\neq i$のニクラス分類としてとらえる。このとき$y=i$に対するy_predを$y=i$である確率として扱い、最大のy_predのクラスに分類する。

  

## (4) 変数bの最適化

> 交差エントロピー誤差関数
> $$L=-\frac{1}{n}\sum_{i=1}^{n} \bigl\{y^{(i)}\textrm{log}f(x^{(i)})+(1-y^{(i)})\textrm{log}(1-f(x^{(i)}))\bigr\}$$
> を損失関数として用いる。また、最適化には勾配法などを使う。

## (5) 最適化の際の注意

> (4)の最適化法をすべてのデータを用いて行うと過学習が起こり、用いたデータにしか適用できないモデルが形成される恐れがある。
> そのため、ホールドアウト法や交差検証によって訓練用のデータが検証データにも適用できるように妥当性を検討する必要がある。