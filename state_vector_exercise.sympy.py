from sympy.physics.quantum import \
    OrthogonalKet, Dagger, qapply
from sympy import sqrt
𝝍 = (OrthogonalKet(0) + sqrt(3) * OrthogonalKet(1)) / 2
𝑥 = OrthogonalKet(1)
print(
    qapply(Dagger(𝝍) * 𝝍),
    (Dagger(𝑥) * 𝑥).doit(),
    abs(qapply(Dagger(𝝍) * 𝑥)) ** 2)
