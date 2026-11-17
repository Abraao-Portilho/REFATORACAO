
from datetime import date

from refatoracao.q1.purchase_email_service import (
    Address,
    Purchase,
    PurchaseEmailService,
    PurchaseItem,
)


def test_build_email_should_keep_same_output_after_refactor():
    svc = PurchaseEmailService()

    purchase = Purchase(
        "123",
        "Victor",
        [
            PurchaseItem("Caderno", 2, 15.0),
            PurchaseItem("Caneta", 3, 3.5),
        ],
        False,
        "VIP-20",
        Address("Rua A", "10", "Belém", "66000-000"),
    )

    email = svc.build_email(purchase)

    expected_email = (
        f"Olá, Victor!\n\n"
        f"Seu pedido #123 foi confirmado em {date.today()}.\n\n"
        f"Itens:\n"
        f"- Caderno (2x) : R$ 30.00\n"
        f"- Caneta (3x) : R$ 10.50\n"
        f"\nSubtotal: R$ 40.50\n"
        f"Frete: R$ 14.90\n"
        f"Descontos: R$ 20.00\n"
        f"TOTAL: R$ 35.40\n\n"
        f"Endereço de entrega:\n"
        f"Rua A, 10\n"
        f"Belém - 66000-000\n\n"
        f"Obrigado por comprar com a gente!\n"
    )

    assert email == expected_email
