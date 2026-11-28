from django.db import migrations, models


LEGAL_SPECIALIZATIONS = [
    "Family Law",
    "Criminal Law",
    "Civil Law",
    "Corporate Law",
    "Commercial Law",
    "Employment Law",
    "Labor Law",
    "Property Law",
    "Real Estate Law",
    "Tax Law",
    "Immigration Law",
    "Administrative Law",
    "Constitutional Law",
    "Contract Law",
    "Intellectual Property Law",
    "Inheritance Law",
    "Consumer Protection Law",
    "Banking and Finance Law",
    "Insurance Law",
    "International Law",
    "Environmental Law",
    "Competition Law",
    "Public Procurement Law",
    "Medical Law",
    "Personal Injury Law",
    "Litigation and Dispute Resolution",
    "Data Protection and GDPR",
    "Cybersecurity Law",
    "Bankruptcy and Insolvency Law",
    "Human Rights Law",
]

REAL_ESTATE_SPECIALIZATIONS = [
    "Real Estate Agent",
    "Real Estate Broker",
    "Property Valuation",
    "Property Management",
    "Real Estate Investment Consultant",
    "Residential Property Consultant",
    "Commercial Property Consultant",
    "Land and Agricultural Property Consultant",
    "Property Development Consultant",
    "Rental and Leasing Consultant",
    "Property Sales Consultant",
    "Property Acquisition Consultant",
    "Real Estate Market Analyst",
    "Property Inspection Consultant",
    "Mortgage and Financing Consultant",
    "Real Estate Transaction Consultant",
    "Property Documentation Consultant",
    "Real Estate Portfolio Consultant",
    "Construction and Development Consultant",
    "Property Tax Consultant",
]


def populate_categories(apps, schema_editor):
    Specializations = apps.get_model("experts", "Specializations")
    manager = Specializations.objects.using(schema_editor.connection.alias)
    manager.filter(name__in=LEGAL_SPECIALIZATIONS).update(category="Legal")
    manager.filter(name__in=REAL_ESTATE_SPECIALIZATIONS).update(category="Real Estate")


def clear_categories(apps, schema_editor):
    Specializations = apps.get_model("experts", "Specializations")
    manager = Specializations.objects.using(schema_editor.connection.alias)
    names = LEGAL_SPECIALIZATIONS + REAL_ESTATE_SPECIALIZATIONS
    manager.filter(name__in=names).update(category=None)


class Migration(migrations.Migration):

    dependencies = [
        ("experts", "0002_initial_specializations"),
    ]

    operations = [
        migrations.AddField(
            model_name="specializations",
            name="category",
            field=models.CharField(
                choices=[("Real Estate", "Real Estate"), ("Legal", "Legal")],
                max_length=12,
                null=True,
            ),
        ),
        migrations.RunPython(populate_categories, clear_categories),
    ]
