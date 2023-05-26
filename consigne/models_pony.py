from pony.orm import Database, Required, Optional, Set, PrimaryKey, Index
from pony.orm import db_session, select
from datetime import date

# Configurer la connexion à la base de données
db = Database(provider='mysql', host='localhost', user='username', password='password', database='database_name')


# Définir les modèles de données
class Departement(db.Entity):
    code_dept = PrimaryKey(str, max_len=2)
    nom_dept = Optional(str, default=None)
    ordre_aff_dept = Optional(int, default=0)


class Commune(db.Entity):
    id = PrimaryKey(int, auto=True)
    dep = Required(Departement, column='dep')
    cp = Optional(str, max_len=5, default=None)
    ville = Optional(str, max_len=50, default=None)
    Index(dep, cp, ville, name='commune_index')


class Client(db.Entity):
    codcli = PrimaryKey(int, auto=True)
    genrecli = Optional(str, max_len=8, default=None)
    nomcli = Optional(str, max_len=40, default=None, index=True)
    prenomcli = Optional(str, max_len=30, default=None)
    adresse1cli = Optional(str, max_len=50, default=None)
    adresse2cli = Optional(str, max_len=50, default=None)
    adresse3cli = Optional(str, max_len=50, default=None)
    villecli_id = Optional(int)
    telcli = Optional(str, max_len=10, default=None)
    emailcli = Optional(str, max_len=255, default=None)
    portcli = Optional(str, max_len=10, default=None)
    newsletter = Optional(int)


class Commande(db.Entity):
    codcde = PrimaryKey(int, auto=True)
    datcde = Required(date)
    codcli = Required(Client, column='codcli')
    timbrecli = Optional(float)
    timbrecde = Optional(float)
    nbcolis = Optional(int, default=1)
    cheqcli = Optional(float)
    idcondit = Optional(int, default=0)
    cdeComt = Optional(str, max_len=255, default=None)
    barchive = Optional(int, default=0)
    bstock = Optional(int, default=0)
    Index(cdeComt, codcli, name='commande_index')


class Conditionnement(db.Entity):
    idcondit = PrimaryKey(int, auto=True)
    libcondit = Optional(str, max_len=50, default=None)
    poidscondit = Optional(int)
    prixcond = Optional(float, default=0.0000)
    ordreimp = Optional(int)
    objets = Set('ObjetCond')


class Objet(db.Entity):
    codobj = PrimaryKey(int, auto=True)
    libobj = Optional(str, max_len=50, default=None)
    tailleobj = Optional(str, max_len=50, default=None)
    puobj = Optional(float, default=0.0000)
    poidsobj = Optional(float, default=0.0000)
    indispobj = Optional(int, default=0)
    o_imp = Optional(int, default=0)
    o_aff = Optional(int, default=0)
    o_cartp = Optional(int, default=0)
    points = Optional(int, default=0)
    o_ordre_aff = Optional(int, default=0)
    condit = Set('ObjetCond')


class ObjetCond(db.Entity):
    idrelcond = PrimaryKey(int, auto=True)
    qteobjdeb = Optional(int, default=0)
    qteobjfin = Optional(int, default=0)
    codobj = Required(Objet, column='codobj')
    codcond = Required(Conditionnement, column='codcond')
    objets = Set(Objet)
    condit = Set(Conditionnement)


class Detail(db.Entity):
    id = PrimaryKey(int, auto=True)
    codcde = Required(Commande, column='codcde')
    qte = Optional(int, default=1)
    colis = Optional(int, default=1)
    commentaire = Optional(str, max_len=100, default=None)


class DetailObjet(db.Entity):
    id = PrimaryKey(int, auto=True)
    detail_id = Required(Detail, column='detail_id')
    objet_id = Required(Objet, column='objet_id')


class Enseigne(db.Entity):
    id_enseigne = PrimaryKey(int, auto=True)
    lb_enseigne = Optional(str, max_len=50, default=None)
    ville_enseigne = Optional(str, max_len=50, default=None)
    dept_enseigne = Optional(int, default=0)


class Poids(db.Entity):
    id = PrimaryKey(int, auto=True)
    valmin = Optional(float, default=0)
    valtimbre = Optional(float, default=0)


class Vignette(db.Entity):
    id = PrimaryKey(int, auto=True)
    valmin = Optional(float, default=0)
    valtimbre = Optional(float, default=0)


class Role(db.Entity):
    codrole = PrimaryKey(int, auto=True)
    librole = Optional(str, max_len=25, default=None)


class Utilisateur(db.Entity):
    code_utilisateur = PrimaryKey(int, auto=True)
    nom_utilisateur = Optional(str, max_len=50, default=None)
    prenom_utilisateur = Optional(str, max_len=50, default=None)
    username = Optional(str, max_len=50, default=None)
    couleur_fond_utilisateur = Optional(int, default=0)
    date_insc_utilisateur = Optional(date)


class RoleUtilisateur(db.Entity):
    id = PrimaryKey(int, auto=True)
    utilisateur_id = Required(Utilisateur, column='utilisateur_id')
    role_id = Required(Role, column='role_id')


# Générer les tables dans la base de données
db.generate_mapping(create_tables=True)
