# CartPole 환경에서의 Qnet 설명

In the CartPole problem, there are four states (displacement, angle, velocity, angular velocity ; continuous) and one action (left or right ; discrete).

Denote states by $s^{(1)},s^{(2)},s^{(3)},s^{(4)}$ and actions by $a$.
For each
$$s=\left(s^{(1)}, s^{(2)}, s^{(3)}, s^{(4)}\right)$$
and $a\in\{0,1\},$
<!-- $$a=\left(a^{(1)}, a^{(2)}\right),$$ -->
we have to specify $Q(s,a)\in\mathbb R$.
To this aim, we construct a NN called `Qnet` whose imput dimension is $|\mathcal S|=4$ and whose output dimension is $|\mathcal A|=2$;
$$
\text{Qnet}:\mathbb R^4\to\mathbb R^2
$$

If $\text{Qnet}\left(s_0^{(1)}, s_0^{(2)}, s_0^{(3)}, s_0^{(4)}\right)=(Q_0,Q_1)$ for some $s_0=\left(s_0^{(1)}, s_0^{(2)}, s_0^{(3)}, s_0^{(4)}\right)$, it means that

$$
\begin{align*}
Q(s_0,0)&=Q_0\\
Q(s_0,1)&=Q_1.
\end{align*}
$$