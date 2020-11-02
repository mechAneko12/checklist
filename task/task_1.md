
## <span style = "color: Deepskyblue"> Simultaneous Control of multiple functions of bionic hand prostheses: Performance and robustness in end users</span>

> - #  ***概要*** <br>
>   この論文は回帰モデルは線形回帰(<span style = "color: Red">LR</span>)を用いて8チャンネルの筋電センサーからの信号から多自由度の義手を制御するモデルとその実装の評価についてです。実際に筋電義手を日常で使っている切断者を被験者として <br>
> 　比較する手法は実際の筋電義手で用いられているCo-contraction control(<span style = "color: Yellow">CC</span>), Slope control(<span style = "color: Green">SC</span>)で、前腕の屈筋と伸筋の2チャンネルの筋電センサーのデータに基づくものです。 <br>
> 　評価指標として、ボックスブロックテストと洗濯ばさみの付け替えテストを使っています。これは、物の把持と前腕の回内・回外の運動を同時に行うような運動において有用な手法であることを示すためです。 <br>
> - **実験結果の概要**
>   - ソケットのつけ外しによる影響は予想に反して見られなかった。
>   - 前腕の位置による影響はCCにもっとも見られた。
> 
> 　
> <br>

> - #  ***疑問点のリスト*** <br>
>   - 

> - # ***論文に対する批判・改善案***　<br>
>   - 比較としてCC, SCという従来のモデルを提示しているが、実用化されている物のほかにも8チャンネルのような多数のセンサーによる回帰（CNNなど）との比較もある方が適当なのではないかと考えました。
>   - 
