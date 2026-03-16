# 球面上の測地線：数学的背景

## 1. 設定

単位球面 $S^2$ を $\mathbb{R}^3$ の部分多様体として扱う。

$$S^2 = \{ \mathbf{x} \in \mathbb{R}^3 \mid |\mathbf{x}| = 1 \}$$

球面座標による局所座標系 $(\varphi, \theta)$ は

$$\mathbf{x}(\varphi, \theta) = (\sin\varphi\cos\theta,\ \sin\varphi\sin\theta,\ \cos\varphi), \quad \varphi \in (0, \pi),\ \theta \in [0, 2\pi)$$

## 2. Riemann 計量

$\mathbb{R}^3$ の標準内積を $S^2$ に制限すると、$(\varphi, \theta)$ 座標での計量テンソル $(g_{ij})$ は

$$g = d\varphi^2 + \sin^2\varphi \, d\theta^2$$

すなわち $g_{\varphi\varphi} = 1$、$g_{\theta\theta} = \sin^2\varphi$、$g_{\varphi\theta} = 0$。

## 3. 測地線方程式

曲線 $\gamma(t) = (\varphi(t), \theta(t))$ が測地線であるとは、弧長を極小にする（局所的な最短曲線の）条件として導かれる **測地線方程式** を満たすことである。

$$\ddot{u}^k + \Gamma^k_{ij} \dot{u}^i \dot{u}^j = 0 \quad (k = 1, 2)$$

ここで $\Gamma^k_{ij}$ は Levi-Civita 接続の Christoffel 記号。$S^2$ における非零成分は

$$\Gamma^\varphi_{\theta\theta} = -\sin\varphi\cos\varphi, \qquad \Gamma^\theta_{\varphi\theta} = \Gamma^\theta_{\theta\varphi} = \cot\varphi$$

これを代入すると測地線方程式は

$$\ddot{\varphi} - \sin\varphi\cos\varphi\,\dot{\theta}^2 = 0$$
$$\ddot{\theta} + 2\cot\varphi\,\dot{\varphi}\dot{\theta} = 0$$

この連立 ODE の解が $S^2$ 上の測地線である。

## 4. 大円が測地線であること

上の方程式を直接解く代わりに、埋め込みを利用する方が見通しが良い。

**命題**: $S^2$ 上の測地線は、原点を通る平面と $S^2$ の交わりである **大円** に限られる。

**証明の骨格**:

$\mathbb{R}^3$ における曲線 $\gamma$ が $S^2$ 上にあるとき、$\gamma$ が $S^2$ の測地線である必要十分条件は

$$\ddot{\gamma}(t) \parallel \gamma(t)$$

すなわち加速度ベクトルが常に $\gamma(t)$ の法線方向（球の中心方向）を向くことである。これは $S^2$ の第二基本形式が $\mathrm{II}(\mathbf{v}, \mathbf{v}) = -|\mathbf{v}|^2 \mathbf{n}$（$\mathbf{n}$ は外向き単位法線）で与えられることと、測地線の定義 $\nabla_{\dot\gamma}\dot\gamma = 0$ から従う。

大円 $\gamma(t) = \cos(t)\,\mathbf{p} + \sin(t)\,\mathbf{v}$（$|\mathbf{p}|=|\mathbf{v}|=1$、$\mathbf{p} \perp \mathbf{v}$）を微分すると

$$\dot{\gamma}(t) = -\sin(t)\,\mathbf{p} + \cos(t)\,\mathbf{v}, \qquad \ddot{\gamma}(t) = -\cos(t)\,\mathbf{p} - \sin(t)\,\mathbf{v} = -\gamma(t)$$

よって $\ddot{\gamma} = -\gamma \parallel \gamma$ が成立し、大円は測地線である。逆に、与えられた点と接線方向に対して測地線は（パラメータ変換を除いて）一意であるから、すべての測地線は大円である。

## 5. 弧長パラメータ化

上の大円は等速パラメータ化されている（$|\dot{\gamma}| \equiv 1$）。

$$|\dot{\gamma}(t)|^2 = \sin^2 t + \cos^2 t = 1$$

したがって $t$ は弧長パラメータそのものであり、$t$ が $[0, 2\pi]$ を動くとき $\gamma$ は大円を一周する。

半径 $r$ の球面での大円は

$$\gamma(t) = r\bigl(\cos(t)\,\mathbf{p} + \sin(t)\,\mathbf{v}\bigr)$$

と書け、弧長は $rt$ となる。

## 6. 接ベクトル基底と初期方向の指定

球面座標 $(\varphi_0, \theta_0)$ における点 $\mathbf{p}$ の接空間の正規直交基底は

$$\mathbf{e}_\varphi = \partial_\varphi \mathbf{x} = (\cos\varphi_0\cos\theta_0,\ \cos\varphi_0\sin\theta_0,\ -\sin\varphi_0)$$
$$\mathbf{e}_\theta = \frac{\partial_\theta \mathbf{x}}{|\partial_\theta \mathbf{x}|} = (-\sin\theta_0,\ \cos\theta_0,\ 0)$$

初期方向角 $\alpha \in [0, \pi)$（$[0, 2\pi)$ ではなく $[0, \pi)$ で十分：反対方向は同じ大円を逆向きにたどるため）を与えると、初期接ベクトルは

$$\mathbf{v} = \cos\alpha\,\mathbf{e}_\varphi + \sin\alpha\,\mathbf{e}_\theta$$

これにより大円が一意に決まる。

## 7. 任意の接ベクトルからの大円構築

数値的に接ベクトル $\mathbf{w}$ が与えられたとき（$\mathbf{p}$ に直交していない場合を含む）、まず接平面への射影と正規化を行う。

$$\mathbf{v} = \frac{\mathbf{w} - (\mathbf{w} \cdot \mathbf{p})\,\mathbf{p}}{|\mathbf{w} - (\mathbf{w} \cdot \mathbf{p})\,\mathbf{p}|}$$

この $\mathbf{v}$ を用いて $\gamma(t) = r(\cos t\,\mathbf{p} + \sin t\,\mathbf{v})$ とすればよい。

## 8. 行列指数関数による導出

Section 4 では大円を「答えとして与えて検証する」形を取ったが、行列指数関数を使うと測地線方程式から $\gamma(t) = \cos(t)\mathbf{p} + \sin(t)\mathbf{v}$ を**直接導出**できる。

### 一階系への書き換え

$\ddot{\gamma} = -\gamma$ は $\mathbb{R}^3$ での線形 ODE であり、状態ベクトル $\mathbf{u} = (\gamma,\ \dot{\gamma})^\top \in \mathbb{R}^6$ を導入すると一階系

$$\dot{\mathbf{u}} = A\mathbf{u}, \qquad A = \begin{pmatrix} O & I \\ -I & O \end{pmatrix}$$

に帰着する（$I$ は $3\times 3$ 単位行列）。

### 行列指数関数の計算

$A^2 = -I_6$ が成り立つことを確認する。

$$A^2 = \begin{pmatrix} O & I \\ -I & O \end{pmatrix}^2 = \begin{pmatrix} -I & O \\ O & -I \end{pmatrix} = -I_6$$

べき級数展開 $e^{tA} = \sum_{n=0}^\infty \frac{t^n A^n}{n!}$ において、$A^2 = -I_6$ から

$$A^{2k} = (-1)^k I_6, \qquad A^{2k+1} = (-1)^k A$$

偶数項と奇数項を分けてまとめると

$$e^{tA} = \left(\sum_{k=0}^\infty \frac{(-1)^k t^{2k}}{(2k)!}\right) I_6 + \left(\sum_{k=0}^\infty \frac{(-1)^k t^{2k+1}}{(2k+1)!}\right) A = \cos(t)\,I_6 + \sin(t)\,A$$

ブロック行列の形で書くと

$$e^{tA} = \begin{pmatrix} \cos(t)\,I & \sin(t)\,I \\ -\sin(t)\,I & \cos(t)\,I \end{pmatrix}$$

これは虚数単位 $i$ に対する Euler の公式 $e^{it} = \cos t + i\sin t$ の行列版そのものであり、$A$ が「$\mathbb{R}^6$ 上の $i$ の役割を果たす行列」であることを意味する。

### 解の表示

初期条件 $\gamma(0) = \mathbf{p}$、$\dot{\gamma}(0) = \mathbf{v}$（$|\mathbf{p}| = |\mathbf{v}| = 1$、$\mathbf{p} \perp \mathbf{v}$）のもとで

$$\begin{pmatrix} \gamma(t) \\ \dot{\gamma}(t) \end{pmatrix} = e^{tA} \begin{pmatrix} \mathbf{p} \\ \mathbf{v} \end{pmatrix} = \begin{pmatrix} \cos(t)\,\mathbf{p} + \sin(t)\,\mathbf{v} \\ -\sin(t)\,\mathbf{p} + \cos(t)\,\mathbf{v} \end{pmatrix}$$

上の行が $\gamma(t) = \cos(t)\,\mathbf{p} + \sin(t)\,\mathbf{v}$ を与える。

### 補足：測地線方程式が線形になる理由

球面座標での測地線方程式（Section 3）は $\sin\varphi$ などの非線形項を含む。それが $\mathbb{R}^3$ に埋め込んだ途端に線形になるのは、**曲率が定数**の空間形（space form）である $S^2$ の特殊性による。双曲面 $H^2$ でも同様の構造があり、$A^2 = +I_6$ から $e^{tA} = \cosh(t)\,I_6 + \sinh(t)\,A$ となって測地線が双曲関数で表される。

## 9. 手計算の手順まとめ

球面上の点 $P = (\varphi_0, \theta_0)$ から方向角 $\alpha$ の測地線を求めるには：

1. $\mathbf{p} = \mathbf{x}(\varphi_0, \theta_0)$ を計算する
2. $\mathbf{e}_\varphi$、$\mathbf{e}_\theta$ を求める
3. $\mathbf{v} = \cos\alpha\,\mathbf{e}_\varphi + \sin\alpha\,\mathbf{e}_\theta$ とする
4. 大円 $\gamma(t) = \cos(t)\,\mathbf{p} + \sin(t)\,\mathbf{v}$ を書き下す
5. 必要なら $\gamma(t)$ を球面座標に戻す：$\varphi(t) = \arccos(\gamma_z(t))$、$\theta(t) = \mathrm{atan2}(\gamma_y(t), \gamma_x(t))$

球面座標での測地線方程式（Section 3）を直接解くより、この埋め込みを経由する方法のほうが計算量が少なく、数値実装も安定している。
