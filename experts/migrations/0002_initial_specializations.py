from django.db import migrations


SPECIALIZATIONS = [
    ("Family Law", "Advises on marriage, divorce, child arrangements, adoption, and other family matters."),
    ("Criminal Law", "Advises on criminal charges, investigations, defense strategy, and sentencing matters."),
    ("Civil Law", "Handles non-criminal disputes involving individuals, organizations, and civil legal rights."),
    ("Corporate Law", "Advises companies on formation, governance, restructuring, compliance, and business transactions."),
    ("Commercial Law", "Supports businesses with trade, sales, distribution, and other commercial agreements."),
    ("Employment Law", "Advises employers and employees on workplace rights, contracts, and employment disputes."),
    ("Labor Law", "Handles collective labor relations, unions, workplace standards, and labor disputes."),
    ("Property Law", "Advises on ownership, use, transfer, and protection of real and personal property."),
    ("Real Estate Law", "Guides clients through property purchases, sales, leases, title issues, and real estate disputes."),
    ("Tax Law", "Advises individuals and businesses on tax obligations, planning, audits, and tax disputes."),
    ("Immigration Law", "Assists with visas, residence, citizenship, asylum, and immigration proceedings."),
    ("Administrative Law", "Handles matters involving government agencies, public decisions, permits, and appeals."),
    ("Constitutional Law", "Advises on constitutional rights, government powers, and challenges to public laws or actions."),
    ("Contract Law", "Drafts, reviews, and resolves disputes concerning agreements and contractual obligations."),
    ("Intellectual Property Law", "Protects and manages patents, trademarks, copyrights, designs, and trade secrets."),
    ("Inheritance Law", "Advises on wills, estates, succession, inheritance rights, and probate disputes."),
    ("Consumer Protection Law", "Helps consumers and businesses address unfair practices, defective goods, and consumer rights."),
    ("Banking and Finance Law", "Advises on lending, financial services, banking regulation, and finance transactions."),
    ("Insurance Law", "Handles insurance coverage, policy interpretation, claims, and disputes with insurers."),
    ("International Law", "Advises on cross-border legal matters, treaties, jurisdiction, and international obligations."),
    ("Environmental Law", "Supports compliance with environmental rules and resolves pollution, permitting, and conservation matters."),
    ("Competition Law", "Advises on antitrust rules, market conduct, mergers, and competition authority investigations."),
    ("Public Procurement Law", "Guides suppliers and public bodies through tendering, procurement rules, and bid challenges."),
    ("Medical Law", "Handles legal matters involving healthcare providers, patients, medical standards, and treatment."),
    ("Personal Injury Law", "Assists people seeking compensation for injuries caused by negligence or wrongful conduct."),
    ("Litigation and Dispute Resolution", "Represents clients in court proceedings, arbitration, mediation, and settlement negotiations."),
    ("Data Protection and GDPR", "Advises on personal data privacy, GDPR compliance, data subject rights, and incidents."),
    ("Cybersecurity Law", "Advises on cyber risk obligations, security incidents, digital evidence, and related regulation."),
    ("Bankruptcy and Insolvency Law", "Guides debtors, creditors, and businesses through insolvency and restructuring proceedings."),
    ("Human Rights Law", "Protects fundamental rights and represents people in rights claims and related proceedings."),
    ("Real Estate Agent", "Helps clients buy, sell, or rent property and coordinates viewings, offers, and negotiations."),
    ("Real Estate Broker", "Coordinates property transactions and agent services for buyers, sellers, landlords, and tenants."),
    ("Property Valuation", "Estimates property market value using comparable sales, property condition, and market factors."),
    ("Property Management", "Oversees property operations, tenant relations, maintenance, rent, and owner reporting."),
    ("Real Estate Investment Consultant", "Evaluates property investment opportunities, returns, risks, and portfolio strategy."),
    ("Residential Property Consultant", "Advises clients on residential property selection, pricing, purchase, and sale."),
    ("Commercial Property Consultant", "Advises on offices, retail, industrial property, commercial leases, and transactions."),
    ("Land and Agricultural Property Consultant", "Advises on land and agricultural property use, acquisition, valuation, and sale."),
    ("Property Development Consultant", "Supports development projects with site assessment, planning, feasibility, and delivery advice."),
    ("Rental and Leasing Consultant", "Matches tenants and landlords and advises on rental terms, listings, and lease processes."),
    ("Property Sales Consultant", "Markets property listings and guides sellers and buyers through offers and sales."),
    ("Property Acquisition Consultant", "Finds and assesses properties for clients and supports acquisition negotiations."),
    ("Real Estate Market Analyst", "Researches property trends, comparable values, demand, supply, and market forecasts."),
    ("Property Inspection Consultant", "Assesses property condition and identifies visible defects, maintenance needs, and risks."),
    ("Mortgage and Financing Consultant", "Explains mortgage and property financing options and helps compare suitable terms."),
    ("Real Estate Transaction Consultant", "Coordinates property transaction steps, parties, timelines, and closing requirements."),
    ("Property Documentation Consultant", "Organizes and reviews property records, transaction documents, and ownership paperwork."),
    ("Real Estate Portfolio Consultant", "Advises owners on portfolio performance, asset mix, strategy, and property decisions."),
    ("Construction and Development Consultant", "Advises on construction and development planning, project coordination, and delivery."),
    ("Property Tax Consultant", "Advises property owners on property tax assessments, filings, planning, and appeals."),
]


def add_specializations(apps, schema_editor):
    Specializations = apps.get_model("experts", "Specializations")
    manager = Specializations.objects.using(schema_editor.connection.alias)
    for name, description in SPECIALIZATIONS:
        manager.get_or_create(name=name, defaults={"description": description})


def remove_specializations(apps, schema_editor):
    Specializations = apps.get_model("experts", "Specializations")
    manager = Specializations.objects.using(schema_editor.connection.alias)
    for name, description in SPECIALIZATIONS:
        manager.filter(name=name, description=description).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("experts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_specializations, remove_specializations),
    ]
