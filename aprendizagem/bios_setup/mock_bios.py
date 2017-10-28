from bios_setup import db
from bios_setup.api import models

entity = models.VersaoBios(
    descricao='1.0.1 UEFI'
)
db.session.add(entity)
db.session.commit()

entity = models.VersaoBios(
    descricao='2.0.2 UEFI'
)
db.session.add(entity)
db.session.commit()

entity = models.VersaoBios(
    descricao='3.0.3 UEFI'
)
db.session.add(entity)
db.session.commit()
