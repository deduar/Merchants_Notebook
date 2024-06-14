from datetime import datetime, time
from dotenv import load_dotenv

from coco_merchant_pfm_es.coco_merchant_pfm_es import config_pfm_es, Coco_merchant, Mov

load_dotenv()

merchant = Coco_merchant(conf=config_pfm_es.load(), internal_mode=1)
mov = Mov(
    id="UNO",
    title="Compras mercadona",
    amount="-33.3",
    date="2014-0505",
    category="compras",
    subcategory="otros",
)

print(merchant.merchant_predict(mov))
