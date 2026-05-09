#!/usr/bin/env python3
"""
NEGOCE RATIONEL — Générateur de landing pages SEO
Régénère toutes les pages /<slug>.html depuis ce fichier.
Usage: python3 build_pages.py
"""

from pathlib import Path
from datetime import date
import json
import html as htmlmod

ROOT = Path(__file__).parent
SITE_URL = "https://negocerationel.ma"
TODAY = date.today().isoformat()

# ---------- Données : 9 landing pages SEO ----------
PAGES = [
    {
        "slug": "bac-a-ordures",
        "kw": "Bac à ordures",
        "title": "Bac à Ordures Maroc — PEHD & Galvanisé EN 840-2 | NEGOCE RATIONEL",
        "desc": "Bacs à ordures fabriqués au Maroc : PEHD 50L à 660L et acier galvanisé. Conforme EN 840-2. Pour collectivités, industriels, syndics. Devis sous 24h.",
        "h1": "Bac à ordures fabriqué au Maroc — PEHD &amp; Acier Galvanisé",
        "image": "bac-galvanise-660l.jpg",
        "image_alt": "Bac à ordures galvanisé 660L 4 roues conforme EN 840-2",
        "intro": "Le <strong>bac à ordures</strong> est l'élément central de tout système de collecte des déchets. NEGOCE RATIONEL fabrique au Maroc des bacs à ordures roulants en deux gammes : <strong>PEHD (polyéthylène haute densité)</strong> de 50 L à 660 L et <strong>acier galvanisé à chaud</strong> conforme à la norme européenne EN 840-2. Tous nos bacs sont compatibles avec les systèmes de levage des camions de collecte standard.",
        "h2_blocks": [
            {
                "h2": "Quelle taille de bac à ordures choisir ?",
                "body": "<p>Le choix du volume dépend du nombre d'usagers et de la fréquence de collecte :</p><ul class='space-y-2 mt-3'><li><strong>50 L / 120 L</strong> — usage individuel, maison, petit commerce.</li><li><strong>240 L / 360 L</strong> — petit immeuble, résidence, restaurant, école.</li><li><strong>660 L</strong> — grand immeuble, marché, zone industrielle, point de regroupement collectif.</li></ul>"
            },
            {
                "h2": "Bac à ordures plastique ou galvanisé ?",
                "body": "<p>Le <strong>bac plastique PEHD</strong> est plus léger, économique et idéal pour les ordures ménagères courantes en intérieur ou abrité. Le <strong>bac galvanisé</strong> en acier 2 mm résiste au feu, aux UV, aux chocs et au vandalisme : il est recommandé pour les voies publiques, les sites industriels et les points de collecte intensifs (durée de vie 10-15 ans contre 5-7 ans pour le PEHD).</p>"
            },
            {
                "h2": "Conformité norme EN 840-2",
                "body": "<p>Nos bacs à ordures 660 L respectent la norme <strong>EN 840-2</strong> qui régit : dimensions standard, résistance mécanique, stabilité statique, compatibilité avec les peignes des camions-bennes et endurance des roues. C'est l'assurance d'un matériel pérenne, accepté par toutes les communes et opérateurs de collecte au Maroc.</p>"
            },
            {
                "h2": "Livraison de bacs à ordures partout au Maroc",
                "body": "<p>Depuis notre atelier de Casablanca, nous livrons nos bacs à ordures dans toutes les villes du Maroc : Rabat, Marrakech, Tanger, Fès, Agadir, Oujda, Meknès, Tétouan, Safi, El Jadida, etc. Délai standard : 3 à 10 jours selon la quantité.</p>"
            }
        ],
        "faqs": [
            ("Quel est le prix d'un bac à ordures 660 L au Maroc ?", "Le prix varie selon le matériau (PEHD ou galvanisé), la quantité et la couleur. Demandez un devis gratuit personnalisé : réponse sous 24 h ouvrées."),
            ("Vos bacs à ordures sont-ils livrés montés ?", "Oui, nos bacs à ordures roulants sont livrés montés et prêts à l'emploi, avec roues et couvercle installés."),
            ("Peut-on personnaliser la couleur des bacs à ordures ?", "Oui, vert, bleu, jaune, gris, marron — toutes les couleurs du tri sélectif sont disponibles, ainsi que des couleurs sur charte (peinture poudre).")
        ],
        "products_to_link": ["bac-pehd", "bac-galvanise-660", "bac-galvanise-360"]
    },
    {
        "slug": "poubelle-plastique",
        "kw": "Poubelle plastique",
        "title": "Poubelle Plastique PEHD Maroc — 50L à 660L | NEGOCE RATIONEL",
        "desc": "Fabricant marocain de poubelles plastiques en PEHD, capacités 50L, 120L, 240L, 360L et 660L. 4 roues, couleur au choix, conforme EN 840-2. Livraison Maroc.",
        "h1": "Poubelle plastique PEHD — Fabriquée au Maroc",
        "image": "bac-pehd-660l.jpg",
        "image_alt": "Poubelle plastique PEHD 660L 4 roues — bac roulant",
        "intro": "Notre <strong>poubelle plastique</strong> est moulée en <strong>polyéthylène haute densité (PEHD)</strong>, matériau de référence pour la collecte des ordures ménagères. Légère, robuste, facile à nettoyer et résistante aux UV, elle équipe collectivités, syndics, industriels et commerces partout au Maroc.",
        "h2_blocks": [
            {
                "h2": "Pourquoi choisir une poubelle plastique en PEHD ?",
                "body": "<p>Le <strong>PEHD</strong> (polyéthylène haute densité) offre le meilleur compromis pour la collecte courante :</p><ul class='space-y-2 mt-3'><li>Léger : facilite la manipulation par les agents de propreté.</li><li>Insensible à la corrosion, ne rouille jamais.</li><li>Recyclable à 100 %.</li><li>Lavable à grande eau, hygiène facile à maintenir.</li><li>Plus économique que les bacs métalliques.</li></ul>"
            },
            {
                "h2": "Toutes les capacités disponibles",
                "body": "<p>Nos poubelles plastiques sont disponibles en 5 capacités standards :</p><ul class='space-y-2 mt-3'><li><strong>50 L</strong> — corbeille intérieure / petit poste de tri.</li><li><strong>120 L</strong> — usage individuel résidentiel.</li><li><strong>240 L</strong> — petit collectif, immeuble.</li><li><strong>360 L</strong> — résidence, école, restaurant.</li><li><strong>660 L</strong> — grand collectif, industrie, marché — conforme EN 840-2.</li></ul>"
            },
            {
                "h2": "Couleurs pour le tri sélectif",
                "body": "<p>Nos poubelles plastiques sont disponibles dans toutes les couleurs du tri sélectif marocain et international : <strong>vert</strong> (verre / végétal), <strong>jaune</strong> (emballages), <strong>bleu</strong> (papier-carton), <strong>marron</strong> (organique), <strong>gris</strong> (ordures ménagères résiduelles). Possibilité de marquage pour collectivités.</p>"
            },
            {
                "h2": "Compatible avec tous les camions de collecte",
                "body": "<p>Nos poubelles plastiques 660 L respectent la norme <strong>EN 840-2</strong> : peigne de levage standard, dimensions normalisées, compatibles avec tous les camions-bennes utilisés au Maroc.</p>"
            }
        ],
        "faqs": [
            ("Une poubelle plastique 660L peut-elle remplacer un bac métallique ?", "Oui dans la plupart des usages collectifs et résidentiels. Pour les zones à risque vandalisme/feu ou industrie lourde, nous recommandons le bac galvanisé."),
            ("Combien d'années dure une poubelle plastique PEHD ?", "Une poubelle PEHD de qualité a une durée de vie de 5 à 7 ans en usage extérieur intensif, jusqu'à 10 ans en usage abrité."),
            ("Le PEHD résiste-t-il au soleil marocain ?", "Oui. Nos poubelles plastiques sont stabilisées anti-UV, conçues pour résister aux conditions climatiques marocaines (températures, ensoleillement intense).")
        ],
        "products_to_link": ["bac-pehd"]
    },
    {
        "slug": "ordures-menageres",
        "kw": "Ordures ménagères",
        "title": "Bacs pour Ordures Ménagères Maroc — Collectivités & Syndics | NEGOCE RATIONEL",
        "desc": "Solutions complètes pour la collecte des ordures ménagères au Maroc : bacs PEHD, conteneurs galvanisés, bennes. Conforme EN 840-2. Fabrication marocaine.",
        "h1": "Bacs pour la collecte des ordures ménagères",
        "image": "bac-galvanise-660l.jpg",
        "image_alt": "Bac pour ordures ménagères 660L conforme EN 840-2",
        "intro": "La gestion des <strong>ordures ménagères</strong> exige un matériel technique fiable, hygiénique et compatible avec les systèmes de collecte municipaux. NEGOCE RATIONEL équipe communes, syndics, sociétés de gestion des déchets et industriels au Maroc avec des bacs et conteneurs adaptés à chaque flux.",
        "h2_blocks": [
            {
                "h2": "Qu'appelle-t-on « ordures ménagères » ?",
                "body": "<p>Les <strong>ordures ménagères</strong> regroupent les déchets produits quotidiennement par les ménages : restes alimentaires, emballages, papiers, plastiques, verres, textiles… Au Maroc, leur gestion est une compétence communale, encadrée par la loi 28-00 sur la gestion des déchets.</p>"
            },
            {
                "h2": "Quel bac pour les ordures ménagères résiduelles ?",
                "body": "<p>Pour le flux résiduel (non trié) en habitat collectif, le standard est le <strong>bac roulant 660 L</strong>, en PEHD ou galvanisé, conforme EN 840-2. Pour l'individuel, on utilise un <strong>bac 120 L ou 240 L</strong>. Les zones à fort vandalisme (rue ouverte, zones industrielles) bénéficient du <strong>bac galvanisé</strong>.</p>"
            },
            {
                "h2": "Tri sélectif des ordures ménagères",
                "body": "<p>Nous fournissons les bacs colorés du tri sélectif : <strong>jaune</strong> pour les emballages recyclables, <strong>bleu</strong> pour le papier-carton, <strong>vert</strong> pour le verre, <strong>marron</strong> pour la matière organique, <strong>gris</strong> pour les ordures ménagères résiduelles. Possibilité de logo communal ou consignes de tri imprimées.</p>"
            },
            {
                "h2": "Pour qui ?",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Communes &amp; arrondissements</strong> — équipement des points de regroupement.</li><li><strong>Syndics &amp; promoteurs immobiliers</strong> — local poubelles d'immeuble.</li><li><strong>Sociétés délégataires</strong> de la collecte urbaine.</li><li><strong>Hôtels, restaurants, écoles</strong>.</li><li><strong>Industriels</strong> — déchets non dangereux assimilables.</li></ul>"
            }
        ],
        "faqs": [
            ("Combien de litres pour un immeuble de 20 logements ?", "Compter environ 30 à 40 L par logement par semaine pour les ordures ménagères résiduelles, soit 2 à 3 bacs 660 L collectés 2 fois par semaine."),
            ("Comment éviter les odeurs ?", "Couvercle bien fermé, lavage régulier à grande eau, et stocker les bacs à l'abri du soleil direct. Nos couvercles plastiques sont étanches."),
            ("Vendez-vous aux particuliers ?", "Notre cible principale est le B2B (collectivités, syndics, industriels), mais nous acceptons les commandes particulières à partir de 1 unité — devis gratuit.")
        ],
        "products_to_link": ["bac-pehd", "bac-galvanise-660", "bac-galvanise-360"]
    },
    {
        "slug": "caisson-metallique",
        "kw": "Caisson métallique",
        "title": "Caisson Métallique 5/6 m³ Maroc — Industrie & Chantiers | NEGOCE RATIONEL",
        "desc": "Caissons métalliques 5 à 6 m³ en acier renforcé soudé pour chantiers, industries et déchets volumineux. Fabrication marocaine, livraison Maroc, devis 24h.",
        "h1": "Caisson métallique 5 / 6 m³ — Acier renforcé soudé",
        "image": "caisson-metallique.jpg",
        "image_alt": "Caisson métallique benne industrielle 5/6 m³ acier renforcé",
        "intro": "Le <strong>caisson métallique</strong> est la solution de collecte volumineuse incontournable pour les <strong>chantiers BTP</strong>, les <strong>sites industriels</strong> et les <strong>déchèteries</strong>. NEGOCE RATIONEL fabrique au Maroc des caissons soudés en acier renforcé, adaptés aux camions multi-bennes et aux usages les plus exigeants.",
        "h2_blocks": [
            {
                "h2": "Caractéristiques techniques",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Volume :</strong> 5 à 6 m³ standard (autres volumes sur demande).</li><li><strong>Matière :</strong> acier renforcé, tôle d'épaisseur 3 à 5 mm selon usage.</li><li><strong>Construction :</strong> soudée intégralement, sans rivet.</li><li><strong>Renforts :</strong> cornières, traverses inférieures.</li><li><strong>Compatible :</strong> camions multibennes (Ampliroll, lève-conteneur).</li><li><strong>Couleur :</strong> au choix, peinture antirouille.</li></ul>"
            },
            {
                "h2": "Usages typiques du caisson métallique",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Chantiers BTP</strong> — gravats, ferraille, bois, déchets de démolition.</li><li><strong>Industries</strong> — déchets de production volumineux.</li><li><strong>Déchèteries communales</strong> — collecte par flux.</li><li><strong>Métiers du recyclage</strong> — acheminement vers centres de tri.</li><li><strong>Marchés &amp; foires</strong> — collecte de fin d'événement.</li></ul>"
            },
            {
                "h2": "Caisson galvanisé ou peint ?",
                "body": "<p>Pour un usage en environnement humide (proximité mer, pluie fréquente, déchets organiques), nous recommandons la <strong>galvanisation à chaud</strong> qui multiplie la durée de vie par 3. Pour un usage chantier classique, la <strong>peinture antirouille</strong> sur acier nu est plus économique.</p>"
            },
            {
                "h2": "Délais de fabrication",
                "body": "<p>Compte tenu du caractère unitaire et soudé du caisson métallique, le délai standard de fabrication est de <strong>10 à 20 jours ouvrés</strong> après confirmation du devis et de l'acompte. Livraison Maroc entier au départ de Casablanca.</p>"
            }
        ],
        "faqs": [
            ("Quelle différence entre caisson et benne métallique ?", "Les termes sont souvent synonymes au Maroc. Techniquement, la « benne » désigne le contenant lui-même et le « caisson » insiste sur la structure soudée. Nos caissons sont des bennes amovibles compatibles Ampliroll."),
            ("Volume sur mesure possible ?", "Oui. Nous fabriquons sur plan : 4 m³, 7 m³, 10 m³, 15 m³, etc. selon vos contraintes."),
            ("Avec ou sans couvercle ?", "Au choix : couvercle plein, à filet, à vantaux ou sans couvercle selon l'usage.")
        ],
        "products_to_link": ["caisson-metallique"]
    },
    {
        "slug": "conteneur-galvanise",
        "kw": "Conteneur galvanisé",
        "title": "Conteneur Galvanisé EN 840-2 Maroc — Acier 2mm | NEGOCE RATIONEL",
        "desc": "Conteneurs en acier galvanisé à chaud 360L et 660L, conformes EN 840-2. Fabrication marocaine, durée de vie 10-15 ans. Pour collectivités et industries.",
        "h1": "Conteneur galvanisé — Acier 2 mm conforme EN 840-2",
        "image": "bac-galvanise-660l.jpg",
        "image_alt": "Conteneur galvanisé 660L 4 roues acier 2mm EN 840-2",
        "intro": "Le <strong>conteneur galvanisé</strong> est la solution premium pour la collecte intensive des déchets. Fabriqué en <strong>acier galvanisé à chaud</strong> de 2 mm minimum, il offre une résistance au feu, aux chocs, aux UV et au vandalisme inégalée. Notre gamme, conforme à la norme européenne EN 840-2, équipe les plus grandes collectivités marocaines.",
        "h2_blocks": [
            {
                "h2": "Pourquoi le galvanisé est-il supérieur ?",
                "body": "<p>La <strong>galvanisation à chaud</strong> consiste à immerger l'acier dans un bain de zinc fondu à 450 °C : une couche métallurgique d'environ 80 µm protège durablement contre la corrosion. Avantages :</p><ul class='space-y-2 mt-3'><li><strong>Anti-rouille</strong> longue durée même en bord de mer.</li><li><strong>Résiste au feu</strong> contrairement aux poubelles plastiques.</li><li><strong>Résiste au vandalisme</strong> et aux chocs.</li><li><strong>Durée de vie 10 à 15 ans</strong> en usage extérieur intensif.</li></ul>"
            },
            {
                "h2": "Spécifications techniques (660 L)",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Volume :</strong> 660 L</li><li><strong>Matière :</strong> acier galvanisé à chaud, épaisseur 2,0 mm minimum</li><li><strong>Dimensions :</strong> 1370 × 750 × 1160 mm (L × l × H)</li><li><strong>Charge max :</strong> 250 kg</li><li><strong>Roues :</strong> 4 × ⌀200 mm dont 2 avec freins</li><li><strong>Couvercle :</strong> plastique vert</li><li><strong>Norme :</strong> EN 840-2</li></ul>"
            },
            {
                "h2": "Compatibilité collecte",
                "body": "<p>Le conteneur galvanisé 660 L NEGOCE RATIONEL est compatible avec tous les <strong>peignes de levage standard EN 840-2</strong> utilisés par les camions-bennes du Maroc, qu'il s'agisse de matériel européen, turc ou local.</p>"
            },
            {
                "h2": "Pour quels usages ?",
                "body": "<ul class='space-y-2 mt-3'><li>Communes urbaines, points de regroupement de quartier</li><li>Marchés couverts, halles, gares routières</li><li>Sites industriels, zones logistiques</li><li>Hôpitaux, universités, casernes</li><li>Plages, parcs, espaces publics</li></ul>"
            }
        ],
        "faqs": [
            ("Le galvanisé est-il plus cher que le PEHD ?", "Oui à l'achat (typiquement 1,5 à 2× plus cher), mais sa durée de vie est 2 à 3× supérieure. Sur 10 ans, le coût total de possession est inférieur."),
            ("Peut-on peindre un conteneur galvanisé ?", "Oui, après préparation de surface (mordançage). Nous proposons aussi la peinture poudre directement à la commande."),
            ("La galvanisation est-elle traitée à chaud ou électrolytique ?", "Toutes nos galvanisations sont à chaud (au trempé), procédé qui offre la meilleure protection longue durée.")
        ],
        "products_to_link": ["bac-galvanise-660", "bac-galvanise-360"]
    },
    {
        "slug": "corbeille-proprete",
        "kw": "Corbeille de propreté",
        "title": "Corbeille de Propreté Urbaine Maroc — Acier Galvanisé | NEGOCE RATIONEL",
        "desc": "Corbeilles de propreté urbaine en acier galvanisé pour rues, parcs, plages et espaces publics. Fabrication marocaine, anti-vandalisme. Devis sous 24h.",
        "h1": "Corbeille de propreté urbaine — Acier galvanisé",
        "image": "bac-galvanise-360l.jpg",
        "image_alt": "Corbeille de propreté urbaine en acier galvanisé",
        "intro": "La <strong>corbeille de propreté</strong> est le complément indispensable des bacs de collecte pour assurer la propreté des espaces publics. NEGOCE RATIONEL fabrique au Maroc une gamme de corbeilles urbaines en acier galvanisé, robustes, anti-vandalisme et adaptées aux conditions climatiques locales.",
        "h2_blocks": [
            {
                "h2": "Où installer une corbeille de propreté ?",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Voies piétonnes</strong> et trottoirs commerçants</li><li><strong>Parcs et jardins</strong> publics</li><li><strong>Plages et corniches</strong> — résistance à l'air marin essentielle</li><li><strong>Marchés et halles</strong></li><li><strong>Cimetières, lieux de culte</strong></li><li><strong>Aires de jeux, écoles, universités</strong></li><li><strong>Stations de bus, parkings publics</strong></li></ul>"
            },
            {
                "h2": "Caractéristiques de nos corbeilles",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Capacités :</strong> 30 L, 50 L, 80 L, 100 L</li><li><strong>Matière :</strong> acier galvanisé à chaud (anti-corrosion)</li><li><strong>Fixation :</strong> sur poteau, mural ou au sol</li><li><strong>Vidage :</strong> seau intérieur amovible ou bascule</li><li><strong>Cendrier :</strong> intégré en option</li><li><strong>Couleur :</strong> au choix (peinture poudre)</li></ul>"
            },
            {
                "h2": "Anti-vandalisme et anti-feu",
                "body": "<p>Nos corbeilles de propreté en acier galvanisé résistent au feu (contrairement aux modèles plastiques), aux chocs et aux tentatives d'arrachement. Elles sont fixées par platine vissée ou scellement chimique. Idéal pour les zones sensibles.</p>"
            },
            {
                "h2": "Personnalisation pour collectivités",
                "body": "<p>Logo communal, blason, message « Gardons la ville propre », couleurs de la charte municipale : nous personnalisons les corbeilles pour chaque collectivité. Marquage par sérigraphie ou plaque rivetée.</p>"
            }
        ],
        "faqs": [
            ("Combien de corbeilles par km de rue ?", "Recommandation usuelle : 1 corbeille tous les 50 à 100 m en zone commerciale dense, 1 tous les 200 m en zone résidentielle."),
            ("Avec ou sans cendrier ?", "Au choix. Nous proposons un cendrier intégré sur le couvercle (recommandé en zone fumeurs) ou un modèle simple."),
            ("Quelle est la résistance au vol ?", "Fixation par platine vissée + écrous frein ou scellement chimique = inviolable sans outils lourds.")
        ],
        "products_to_link": ["bac-galvanise-360"]
    },
    {
        "slug": "bacs-a-dechets",
        "kw": "Bacs à déchets",
        "title": "Bacs à Déchets Industriels Maroc — Tri Sélectif & DIB | NEGOCE RATIONEL",
        "desc": "Bacs à déchets industriels et tertiaires : PEHD, galvanisé, caissons. Tri sélectif DIB, DEEE, DAS. Fabrication marocaine, conforme EN 840-2.",
        "h1": "Bacs à déchets industriels &amp; tertiaires",
        "image": "bac-pehd-660l.jpg",
        "image_alt": "Bac à déchets PEHD 660L pour tri sélectif industriel",
        "intro": "Pour la gestion professionnelle des déchets, les <strong>bacs à déchets</strong> doivent être adaptés à chaque flux : <strong>DIB</strong> (Déchets Industriels Banals), emballages, papier-carton, organiques, déchets dangereux. NEGOCE RATIONEL équipe industriels, tertiaires et collectivités avec une gamme complète de bacs à déchets pour le tri sélectif.",
        "h2_blocks": [
            {
                "h2": "Quels bacs pour quels déchets ?",
                "body": "<ul class='space-y-2 mt-3'><li><strong>DIB (résiduel)</strong> — bac PEHD ou galvanisé 240 / 660 L, couvercle gris</li><li><strong>Emballages recyclables</strong> — bac jaune 240 / 660 L</li><li><strong>Papier-carton</strong> — bac bleu 240 / 660 L</li><li><strong>Verre</strong> — bac vert 240 L</li><li><strong>Organiques (biodéchets)</strong> — bac marron PEHD étanche</li><li><strong>Déchets volumineux</strong> — caisson métallique 5-6 m³</li></ul>"
            },
            {
                "h2": "Identification visuelle (signalétique)",
                "body": "<p>Nous fournissons les bacs à déchets dans toutes les couleurs du tri sélectif marocain et international, avec possibilité de marquage : pictogrammes, consignes en français/arabe, logo entreprise. Indispensable pour la conformité aux audits ISO 14001 et HSE.</p>"
            },
            {
                "h2": "Bacs à déchets en zone industrielle",
                "body": "<p>Pour les sites soumis au passage de chariots élévateurs, à des températures extrêmes ou aux chocs, nous recommandons les <strong>bacs galvanisés</strong> 360 L ou 660 L. Pour les déchets organiques liquides ou pâteux, le <strong>PEHD étanche</strong> est obligatoire.</p>"
            },
            {
                "h2": "Conformité et sécurité",
                "body": "<p>Tous nos bacs à déchets respectent la norme <strong>EN 840-2</strong> et sont compatibles avec les opérateurs de collecte agréés au Maroc. Nous accompagnons votre démarche <strong>ISO 14001</strong>, <strong>HSE</strong> et <strong>responsabilité élargie du producteur</strong>.</p>"
            }
        ],
        "faqs": [
            ("Pouvez-vous fournir un parc complet pour usine ?", "Oui. Nous équipons des parcs de 10 à plus de 500 bacs à déchets, avec étude personnalisée des flux et signalétique."),
            ("Bacs avec serrure pour déchets sensibles ?", "Oui, sur demande pour les DASRI, déchets confidentiels ou produits dangereux."),
            ("Délai pour 100 bacs PEHD ?", "Stock permanent en couleurs standards : livraison sous 7 à 10 jours selon destination.")
        ],
        "products_to_link": ["bac-pehd", "bac-galvanise-660", "caisson-metallique"]
    },
    {
        "slug": "materiel-technique-proprete",
        "kw": "Matériel technique de propreté",
        "title": "Matériel Technique de Propreté Urbaine Maroc | NEGOCE RATIONEL",
        "desc": "Tout le matériel technique pour la propreté urbaine au Maroc : bacs, conteneurs, caissons, bennes, corbeilles. Fabrication marocaine, normes EN 840-2.",
        "h1": "Matériel technique de propreté urbaine",
        "image": "NEGOCE3.jpeg",
        "image_alt": "Matériel technique de propreté urbaine NEGOCE RATIONEL",
        "intro": "Le <strong>matériel technique de propreté urbaine</strong> regroupe l'ensemble des équipements nécessaires à la collecte, au stockage et à l'évacuation des déchets en milieu public et professionnel. NEGOCE RATIONEL est un fabricant marocain de référence depuis plus de 15 ans, fournissant communes, syndics, industriels et opérateurs de collecte sur tout le territoire.",
        "h2_blocks": [
            {
                "h2": "Notre gamme complète",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Bacs roulants PEHD</strong> 50 L, 120 L, 240 L, 360 L, 660 L — tri sélectif</li><li><strong>Conteneurs galvanisés</strong> 360 L et 660 L conformes EN 840-2</li><li><strong>Caissons métalliques</strong> 5 / 6 m³ pour chantiers et industries</li><li><strong>Bennes métalliques</strong> compatibles Ampliroll</li><li><strong>Corbeilles de propreté</strong> urbaines en acier galvanisé</li><li><strong>Solutions sur mesure</strong> selon cahier des charges</li></ul>"
            },
            {
                "h2": "Pourquoi choisir un fabricant marocain ?",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Délais courts</strong> — fabrication locale, pas d'import depuis l'Europe</li><li><strong>Coût maîtrisé</strong> — pas de droits de douane, transport optimisé</li><li><strong>SAV réactif</strong> — pièces détachées et interventions rapides</li><li><strong>Adapté au climat</strong> — matériaux choisis pour la chaleur, l'air marin, les UV</li><li><strong>Soutien à l'industrie nationale</strong> — préférence nationale pour les marchés publics</li></ul>"
            },
            {
                "h2": "Conformité aux normes",
                "body": "<p>Notre matériel technique respecte la norme européenne <strong>EN 840-2</strong> (bacs roulants à déchets), garantissant la compatibilité avec les camions-bennes utilisés au Maroc et la pérennité du matériel.</p>"
            },
            {
                "h2": "Notre processus",
                "body": "<p>1. <strong>Étude</strong> de votre besoin et conseil personnalisé · 2. <strong>Devis</strong> détaillé sous 24 h · 3. <strong>Fabrication</strong> dans nos ateliers de Casablanca · 4. <strong>Livraison</strong> et installation sur site partout au Maroc.</p>"
            }
        ],
        "faqs": [
            ("Êtes-vous référencés pour les marchés publics ?", "Oui, nous fournissons régulièrement les communes urbaines et les sociétés délégataires. Numéro RC, ICE et patente disponibles sur demande."),
            ("Pouvez-vous équiper un nouveau quartier ?", "Oui, du dimensionnement (étude de flux) à la livraison du parc complet, nous accompagnons les promoteurs et collectivités."),
            ("Pièces détachées disponibles ?", "Oui : roues, axes, couvercles, peignes — stock permanent à Casablanca.")
        ],
        "products_to_link": ["bac-pehd", "bac-galvanise-660", "caisson-metallique", "bac-galvanise-360"]
    },
    {
        "slug": "benne-metallique",
        "kw": "Benne métallique",
        "title": "Benne Métallique 5/6 m³ Maroc — Ampliroll Compatible | NEGOCE RATIONEL",
        "desc": "Bennes métalliques amovibles 5 et 6 m³ compatibles Ampliroll, acier renforcé soudé. Fabrication marocaine pour BTP, industrie et déchèteries.",
        "h1": "Benne métallique 5 / 6 m³ — Compatible Ampliroll",
        "image": "caisson-metallique.jpg",
        "image_alt": "Benne métallique amovible 5/6 m³ acier renforcé Ampliroll",
        "intro": "La <strong>benne métallique</strong> est l'équipement de référence pour les chantiers BTP, les industries et les déchèteries au Maroc. NEGOCE RATIONEL fabrique des bennes amovibles soudées en acier renforcé, compatibles avec les camions <strong>multibennes Ampliroll</strong> et les lève-conteneurs.",
        "h2_blocks": [
            {
                "h2": "Spécifications de nos bennes métalliques",
                "body": "<ul class='space-y-2 mt-3'><li><strong>Volumes standard :</strong> 5 m³, 6 m³ (autres volumes 4-15 m³ sur demande)</li><li><strong>Matière :</strong> acier renforcé, tôle 3 à 5 mm</li><li><strong>Construction :</strong> soudée intégralement, longerons + traverses</li><li><strong>Crochet :</strong> compatible Ampliroll DIN 30722</li><li><strong>Couvercle :</strong> au choix (plein, à filet, à vantaux, sans)</li><li><strong>Finition :</strong> peinture antirouille ou galvanisation</li></ul>"
            },
            {
                "h2": "Usages typiques",
                "body": "<ul class='space-y-2 mt-3'><li><strong>BTP</strong> — gravats, ferraille, bois de coffrage, plâtre</li><li><strong>Démolition</strong> — déchets inertes mélangés</li><li><strong>Industrie</strong> — copeaux, ferraille, déchets volumineux</li><li><strong>Recyclage</strong> — collecte de matières par flux</li><li><strong>Déchèteries</strong> — bennes thématiques (bois, ferraille, encombrants)</li><li><strong>Événementiel</strong> — collecte de fin de manifestation</li></ul>"
            },
            {
                "h2": "Benne peinte ou galvanisée ?",
                "body": "<p>Pour un <strong>usage chantier</strong> classique (1 à 3 ans d'utilisation intensive), la benne peinte antirouille est suffisante et plus économique. Pour un <strong>parc longue durée</strong> ou une exposition aux déchets organiques/humides, la <strong>galvanisation à chaud</strong> est fortement recommandée (durée de vie multipliée par 3).</p>"
            },
            {
                "h2": "Marquage et numérotation",
                "body": "<p>Nous proposons le marquage par sérigraphie ou plaque rivetée : numérotation de parc, logo entreprise, mention « propriété de… », classe de déchet. Indispensable pour la traçabilité des bennes louées ou en rotation.</p>"
            }
        ],
        "faqs": [
            ("Délai de fabrication d'une benne 6 m³ ?", "10 à 20 jours ouvrés selon la quantité et les options (couvercle, galvanisation)."),
            ("Bennes pour location ou achat ?", "Nous fabriquons à la vente. Pour la location, nous travaillons avec des sociétés partenaires de gestion de bennes au Maroc."),
            ("Quelle hauteur de chargement ?", "Nos bennes 5-6 m³ standards mesurent ~1,3 à 1,5 m de hauteur extérieure pour permettre un chargement manuel ou par mini-pelle.")
        ],
        "products_to_link": ["caisson-metallique"]
    },
]

# ---------- Données produits pour le maillage interne ----------
PRODUCT_LINKS = {
    "bac-pehd":           {"name": "Bac Roulant PEHD 660L",           "img": "bac-pehd-660l.jpg",      "alt": "Bac roulant PEHD 660L"},
    "bac-galvanise-660":  {"name": "Bac Galvanisé 660L — 4 roues",    "img": "bac-galvanise-660l.jpg", "alt": "Bac galvanisé 660L 4 roues"},
    "bac-galvanise-360":  {"name": "Bac Galvanisé 360L — 2 roues",    "img": "bac-galvanise-360l.jpg", "alt": "Bac galvanisé 360L 2 roues"},
    "caisson-metallique": {"name": "Caisson Métallique 5/6 m³",        "img": "caisson-metallique.jpg", "alt": "Caisson métallique 5/6 m³"},
}


def render_faqs_html(faqs):
    items = []
    for q, a in faqs:
        items.append(f"""        <details class="faq-item group bg-steel-50 hover:bg-brand-50/40 border border-steel-100 hover:border-brand-200 rounded-2xl transition">
          <summary class="cursor-pointer list-none flex items-center justify-between gap-4 p-5 md:p-6 font-semibold text-steel-900">
            <span>{htmlmod.escape(q)}</span>
            <i class="fa-solid fa-plus text-brand-600 transition group-open:rotate-45" aria-hidden="true"></i>
          </summary>
          <div class="px-5 md:px-6 pb-5 md:pb-6 text-steel-700 leading-relaxed">{a}</div>
        </details>""")
    return "\n".join(items)


def render_faq_jsonld(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ]
    }, ensure_ascii=False, indent=2)


def render_breadcrumb_jsonld(slug, kw):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{SITE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": kw,        "item": f"{SITE_URL}/{slug}.html"},
        ]
    }, ensure_ascii=False, indent=2)


def render_product_jsonld(slug, kw, desc, image):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": kw,
        "description": desc,
        "image": f"{SITE_URL}/assets/images/{image}",
        "brand": {"@type": "Brand", "name": "NEGOCE RATIONEL"},
        "manufacturer": {"@id": f"{SITE_URL}/#organization"},
        "countryOfOrigin": "MA",
        "offers": {
            "@type": "Offer",
            "url": f"{SITE_URL}/{slug}.html#contact",
            "availability": "https://schema.org/InStock",
            "priceCurrency": "MAD",
            "price": "0"
        }
    }, ensure_ascii=False, indent=2)


def render_h2_blocks(blocks):
    out = []
    for i, b in enumerate(blocks):
        out.append(f"""    <section class="mb-12" data-aos="fade-up">
      <h2 class="font-display text-2xl md:text-3xl font-bold text-steel-900 mb-4">{b['h2']}</h2>
      <div class="text-steel-700 leading-relaxed text-lg">{b['body']}</div>
    </section>""")
    return "\n".join(out)


def render_related_products(slugs):
    cards = []
    for s in slugs:
        if s not in PRODUCT_LINKS:
            continue
        p = PRODUCT_LINKS[s]
        cards.append(f"""        <a href="/#produits" class="group bg-white rounded-2xl border border-steel-100 hover:border-brand-300 hover:shadow-xl transition overflow-hidden">
          <div class="aspect-square bg-gradient-to-br from-brand-50/60 to-white p-4 flex items-center justify-center">
            <img src="assets/images/{p['img']}" alt="{p['alt']}" loading="lazy" decoding="async" width="1024" height="1024" class="w-full h-full object-contain group-hover:scale-105 transition" />
          </div>
          <div class="p-4">
            <div class="font-bold text-steel-900 mb-1">{p['name']}</div>
            <div class="text-brand-700 text-sm font-semibold inline-flex items-center gap-1">Voir <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i></div>
          </div>
        </a>""")
    return "\n".join(cards)


def render_related_pages(current_slug):
    """Internal links to other landing pages (4 max)."""
    other = [p for p in PAGES if p['slug'] != current_slug][:4]
    items = []
    for p in other:
        items.append(f'<a href="/{p["slug"]}.html" class="px-4 py-2 bg-white border border-steel-200 hover:border-brand-400 hover:bg-brand-50 rounded-full text-sm font-medium text-steel-800 transition">{p["kw"]}</a>')
    return "\n          ".join(items)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#235e33" />

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index,follow,max-image-preview:large" />
  <meta name="geo.region" content="MA-06" />
  <meta name="geo.placename" content="Casablanca" />

  <link rel="canonical" href="{site}/{slug}.html" />

  <meta property="og:locale" content="fr_MA" />
  <meta property="og:site_name" content="NEGOCE RATIONEL" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{site}/{slug}.html" />
  <meta property="og:image" content="{site}/assets/images/{image}" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23235e33'/%3E%3Cpath d='M20 22h24l-2 26a4 4 0 0 1-4 4H26a4 4 0 0 1-4-4Zm6-6h12a3 3 0 0 1 3 3v3H23v-3a3 3 0 0 1 3-3Z' fill='%23bbe1c1'/%3E%3C/svg%3E" />
  <link rel="manifest" href="/manifest.webmanifest" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="image" href="assets/images/{image}" fetchpriority="high" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="assets/styles.css" />

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{ 50:'#f0f9f1',100:'#dcf0de',200:'#bbe1c1',300:'#8ccb98',400:'#5aae6c',500:'#3a924f',600:'#2a763d',700:'#235e33',800:'#1f4b2c',900:'#1a3e26',950:'#0d2415' }},
            steel: {{ 50:'#f6f7f9',100:'#eceef2',200:'#d5dae2',300:'#b1bac9',400:'#8694ab',500:'#677791',600:'#525f78',700:'#444e62',800:'#3a4252',900:'#333947',950:'#21242e' }}
          }},
          fontFamily: {{ sans:['Inter','system-ui','sans-serif'], display:['Playfair Display','serif'] }}
        }}
      }}
    }};
  </script>

  <script type="application/ld+json">
{breadcrumb_jsonld}
  </script>

  <script type="application/ld+json">
{product_jsonld}
  </script>

  <script type="application/ld+json">
{faq_jsonld}
  </script>
</head>
<body class="font-sans bg-white text-steel-900 antialiased">

  <!-- Mini header -->
  <header class="sticky top-0 z-50 bg-white/90 backdrop-blur border-b border-steel-100">
    <div class="container mx-auto px-4 max-w-6xl">
      <div class="flex items-center justify-between h-16">
        <a href="/" class="flex items-center gap-3" aria-label="NEGOCE RATIONEL — Accueil">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center shadow-lg">
            <i class="fa-solid fa-recycle text-white" aria-hidden="true"></i>
          </div>
          <div>
            <div class="font-display font-bold leading-none">NEGOCE</div>
            <div class="text-[10px] font-semibold text-brand-600 tracking-[0.25em]">RATIONEL</div>
          </div>
        </a>
        <nav class="hidden md:flex items-center gap-1 text-sm" aria-label="Navigation">
          <a href="/" class="px-3 py-2 text-steel-700 hover:text-brand-700 rounded-lg hover:bg-brand-50">Accueil</a>
          <a href="/#produits" class="px-3 py-2 text-steel-700 hover:text-brand-700 rounded-lg hover:bg-brand-50">Produits</a>
          <a href="/#faq" class="px-3 py-2 text-steel-700 hover:text-brand-700 rounded-lg hover:bg-brand-50">FAQ</a>
          <a href="/#contact" class="px-3 py-2 text-steel-700 hover:text-brand-700 rounded-lg hover:bg-brand-50">Contact</a>
        </nav>
        <a href="/#contact" class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-brand-600 to-brand-700 text-white text-sm font-semibold rounded-full hover:shadow-lg transition">
          <i class="fa-solid fa-file-invoice" aria-hidden="true"></i>
          Devis Gratuit
        </a>
      </div>
    </div>
  </header>

  <!-- Breadcrumb -->
  <nav aria-label="Fil d'Ariane" class="bg-steel-50 border-b border-steel-100">
    <div class="container mx-auto px-4 max-w-6xl py-3 text-sm text-steel-600">
      <a href="/" class="hover:text-brand-700">Accueil</a>
      <span class="mx-2 text-steel-400">/</span>
      <span class="text-steel-900 font-semibold">{kw}</span>
    </div>
  </nav>

  <!-- Hero -->
  <section class="relative overflow-hidden bg-gradient-to-br from-brand-950 via-brand-900 to-steel-950 text-white">
    <div class="absolute inset-0 hero-grid opacity-[0.07]" aria-hidden="true"></div>
    <div class="container mx-auto px-4 max-w-6xl py-16 md:py-20 relative">
      <div class="grid md:grid-cols-2 gap-10 items-center">
        <div data-aos="fade-right">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/10 border border-white/20 text-xs mb-5">
            <i class="fa-solid fa-shield-halved text-brand-300" aria-hidden="true"></i>
            <span>Conforme EN 840-2 · Fabriqué au Maroc</span>
          </div>
          <h1 class="font-display text-3xl md:text-5xl font-bold leading-tight mb-5">{h1}</h1>
          <p class="text-lg text-white/80 leading-relaxed mb-8">{intro}</p>
          <div class="flex flex-wrap gap-3">
            <a href="/#contact" class="inline-flex items-center gap-2 px-6 py-3 bg-white text-brand-900 font-bold rounded-full hover:shadow-2xl transition">
              <i class="fa-solid fa-file-invoice-dollar" aria-hidden="true"></i> Demander un devis
            </a>
            <a href="https://wa.me/212722785500?text=Bonjour%2C%20je%20souhaite%20un%20devis%20pour%20{kw_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-6 py-3 border-2 border-white/30 font-semibold rounded-full hover:bg-white/10 transition">
              <i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp
            </a>
          </div>
        </div>
        <div data-aos="fade-left" class="relative aspect-square max-w-md mx-auto">
          <img src="assets/images/{image}" alt="{image_alt}" width="1024" height="1024" loading="eager" fetchpriority="high" decoding="async" class="w-full h-full object-contain drop-shadow-2xl" />
        </div>
      </div>
    </div>
  </section>

  <!-- Article body -->
  <article class="container mx-auto px-4 max-w-3xl py-16">
{h2_blocks}
  </article>

  <!-- Related products -->
  <section class="bg-steel-50 py-16">
    <div class="container mx-auto px-4 max-w-6xl">
      <h2 class="font-display text-3xl font-bold text-center mb-3" data-aos="fade-up">Notre gamme {kw_lower}</h2>
      <p class="text-steel-600 text-center mb-10" data-aos="fade-up">Découvrez les produits associés fabriqués au Maroc.</p>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6" data-aos="fade-up">
{related_products}
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section id="faq" class="py-16 bg-white">
    <div class="container mx-auto px-4 max-w-3xl">
      <h2 class="font-display text-3xl font-bold text-center mb-3" data-aos="fade-up">Questions fréquentes — {kw}</h2>
      <p class="text-steel-600 text-center mb-10" data-aos="fade-up">Tout ce que vous devez savoir avant de commander.</p>
      <div class="space-y-3" data-aos="fade-up">
{faqs_html}
      </div>
    </div>
  </section>

  <!-- Internal links -->
  <section class="bg-steel-50 py-12 border-t border-steel-100">
    <div class="container mx-auto px-4 max-w-4xl text-center">
      <h2 class="font-display text-2xl font-bold mb-4">Découvrir aussi</h2>
      <div class="flex flex-wrap gap-2 justify-center">
          {related_pages}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="py-16 bg-white">
    <div class="container mx-auto px-4 max-w-4xl">
      <div class="bg-gradient-to-br from-brand-600 via-brand-700 to-brand-900 rounded-3xl p-10 md:p-14 text-white text-center" data-aos="zoom-in">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">Besoin d'un devis pour {kw_lower} ?</h2>
        <p class="text-white/85 text-lg mb-8 max-w-xl mx-auto">Réponse sous 24 h ouvrées. Livraison partout au Maroc.</p>
        <div class="flex flex-wrap gap-3 justify-center">
          <a href="/#contact" class="inline-flex items-center gap-2 px-7 py-3.5 bg-white text-brand-800 font-bold rounded-full hover:scale-105 transition shadow-xl">
            <i class="fa-solid fa-file-invoice-dollar" aria-hidden="true"></i> Demander un devis
          </a>
          <a href="tel:+212722785500" class="inline-flex items-center gap-2 px-7 py-3.5 border-2 border-white/30 text-white font-bold rounded-full hover:bg-white/10 transition">
            <i class="fa-solid fa-phone" aria-hidden="true"></i> <span dir="ltr">07.22.78.55.00</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-steel-950 text-white py-10">
    <div class="container mx-auto px-4 max-w-6xl text-center text-sm text-white/60">
      <div class="mb-3">© 2026 NEGOCE RATIONEL — SARL AU, Casablanca, Maroc</div>
      <div class="flex flex-wrap gap-4 justify-center">
        <a href="tel:+212722785500" class="hover:text-brand-400" dir="ltr">07.22.78.55.00</a>
        <a href="mailto:negocerationel@gmail.com" class="hover:text-brand-400" dir="ltr">negocerationel@gmail.com</a>
        <a href="/" class="hover:text-brand-400">Accueil</a>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/212722785500?text=Bonjour%20NEGOCE%20RATIONEL%2C%20je%20souhaite%20un%20devis%20pour%20{kw_url}"
     target="_blank" rel="noopener"
     class="fixed bottom-6 right-6 z-40 w-14 h-14 rounded-full bg-emerald-500 hover:bg-emerald-600 text-white flex items-center justify-center shadow-2xl shadow-emerald-500/40 hover:scale-110 transition"
     aria-label="WhatsApp">
    <i class="fa-brands fa-whatsapp text-2xl" aria-hidden="true"></i>
  </a>

  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js" defer></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.AOS) AOS.init({{ duration: 800, easing: 'ease-out-cubic', once: true, offset: 60 }});
    }});
  </script>
</body>
</html>
"""


def build():
    import urllib.parse
    generated = []
    for page in PAGES:
        slug = page["slug"]
        kw = page["kw"]
        ctx = {
            "site": SITE_URL,
            "slug": slug,
            "kw": kw,
            "kw_lower": kw.lower(),
            "kw_url": urllib.parse.quote(kw),
            "title": page["title"],
            "desc": page["desc"],
            "h1": page["h1"],
            "intro": page["intro"],
            "image": page["image"],
            "image_alt": page["image_alt"],
            "h2_blocks": render_h2_blocks(page["h2_blocks"]),
            "faqs_html": render_faqs_html(page["faqs"]),
            "faq_jsonld": render_faq_jsonld(page["faqs"]),
            "breadcrumb_jsonld": render_breadcrumb_jsonld(slug, kw),
            "product_jsonld": render_product_jsonld(slug, kw, page["desc"], page["image"]),
            "related_products": render_related_products(page["products_to_link"]),
            "related_pages": render_related_pages(slug),
        }
        out = PAGE_TEMPLATE.format(**ctx)
        path = ROOT / f"{slug}.html"
        path.write_text(out, encoding="utf-8")
        generated.append(path.name)
        print(f"  ✓ Generated {path.name} ({len(out):,} bytes)")

    # ---------- Update sitemap.xml ----------
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
               '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
               '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']

    sitemap.append(f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{SITE_URL}/"/>
    <xhtml:link rel="alternate" hreflang="ar" href="{SITE_URL}/?lang=ar"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}/"/>
    <image:image><image:loc>{SITE_URL}/assets/images/bac-galvanise-660l.jpg</image:loc><image:title>Bac galvanisé 660L 4 roues</image:title></image:image>
    <image:image><image:loc>{SITE_URL}/assets/images/bac-pehd-660l.jpg</image:loc><image:title>Bac roulant PEHD 660L</image:title></image:image>
    <image:image><image:loc>{SITE_URL}/assets/images/bac-galvanise-360l.jpg</image:loc><image:title>Bac galvanisé 360L 2 roues</image:title></image:image>
    <image:image><image:loc>{SITE_URL}/assets/images/caisson-metallique.jpg</image:loc><image:title>Caisson métallique 5/6 m³</image:title></image:image>
  </url>
  <url>
    <loc>{SITE_URL}/?lang=ar</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

    for page in PAGES:
        sitemap.append(f"""  <url>
    <loc>{SITE_URL}/{page['slug']}.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <image:image><image:loc>{SITE_URL}/assets/images/{page['image']}</image:loc><image:title>{htmlmod.escape(page['kw'])}</image:title></image:image>
  </url>""")

    sitemap.append('</urlset>\n')
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    print(f"  ✓ Updated sitemap.xml ({len(PAGES) + 2} URLs)")

    return generated


if __name__ == "__main__":
    print("Building NEGOCE RATIONEL landing pages…")
    files = build()
    print(f"\nDone. {len(files)} pages generated.")
