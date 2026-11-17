from refatoracao.q2.password_policy import PasswordPolicy


def test_valid_password_examples():
    policy = PasswordPolicy()
    assert policy.is_valid("SenhaForte1")


def test_invalid_password_examples():
    policy = PasswordPolicy()
    assert not policy.is_valid("curta1A")       # < 10
    assert not policy.is_valid("senhaforte1")   # sem maiúscula
    assert not policy.is_valid("SenhaForteX")   # sem dígito
    assert not policy.is_valid("Senha Forte1")  # espaço


def test_boundary_and_none_inputs():
    policy = PasswordPolicy()
    assert not policy.is_valid(None)
    assert not policy.is_valid("")
    assert policy.is_valid("Senhafort1")      # exatamente 10 caracteres
    assert not policy.is_valid("Senhafor1")   # 9 caracteres
