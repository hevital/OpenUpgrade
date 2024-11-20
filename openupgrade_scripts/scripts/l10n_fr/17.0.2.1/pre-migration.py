# Copyright 2024 Viindoo Technology Joint Stock Company (Viindoo)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade

_account_tax_group_xmlid = [
    "l10n_fr.tax_group_tva_0",
    "l10n_fr.tax_group_tva_20",
    "l10n_fr.tax_group_tva_85",
    "l10n_fr.tax_group_tva_55",
    "l10n_fr.tax_group_tva_10",
    "l10n_fr.tax_group_tva_21",
]

_account_tax_xmlid = [
    "l10n_fr.tva_acq_normale",
    "l10n_fr.tva_acq_specifique",
    "l10n_fr.tva_acq_intermediaire",
    "l10n_fr.tva_acq_reduite",
    "l10n_fr.tva_acq_super_reduite",
    "l10n_fr.tva_purchase_good_fuel",
    "l10n_fr.tva_purchase_good_fuel_TTC",
    "l10n_fr.tva_acq_normale_TTC",
    "l10n_fr.tva_acq_specifique_TTC",
    "l10n_fr.tva_acq_intermediaire_TTC",
    "l10n_fr.tva_acq_reduite_TTC",
    "l10n_fr.tva_acq_super_reduite_TTC",
    "l10n_fr.tva_imm_normale",
    "l10n_fr.tva_imm_specifique",
    "l10n_fr.tva_imm_intermediaire",
    "l10n_fr.tva_imm_reduite",
    "l10n_fr.tva_imm_super_reduite",
    "l10n_fr.tva_import_outside_eu_20",
    "l10n_fr.tva_import_outside_eu_10",
    "l10n_fr.tva_import_outside_eu_8_5",
    "l10n_fr.tva_import_outside_eu_5_5",
    "l10n_fr.tva_import_outside_eu_2_1",
    "l10n_fr.tva_intra_normale_biens",
    "l10n_fr.tva_intra_normale_services",
    "l10n_fr.tva_purchase_service_20_import",
    "l10n_fr.tva_purchase_service_0",
    "l10n_fr.tva_acq_encaissement",
    "l10n_fr.tva_acq_intermediaire_encaissement",
    "l10n_fr.tva_acq_encaissement_reduite",
    "l10n_fr.tva_acq_encaissement_super_reduite",
    "l10n_fr.tva_acq_encaissement_TTC",
    "l10n_fr.tva_acq_intermediaire_encaissement_TTC",
    "l10n_fr.tva_acq_encaissement_reduite_TTC",
    "l10n_fr.tva_acq_encaissement_super_reduite_TTC",
    "l10n_fr.tva_purchase_imm_normale",
    "l10n_fr.tva_normale",
    "l10n_fr.tva_intermediaire",
    "l10n_fr.tva_reduite",
    "l10n_fr.tva_specifique",
    "l10n_fr.tva_super_reduite",
    "l10n_fr.tva_normale_ttc",
    "l10n_fr.tva_intermediaire_ttc",
    "l10n_fr.tva_specifique_ttc",
    "l10n_fr.tva_reduite_ttc",
    "l10n_fr.tva_super_reduite_ttc",
    "l10n_fr.tva_sale_good_0",
    "l10n_fr.tva_sale_good_export_0",
    "l10n_fr.tva_sale_good_intra_0",
    "l10n_fr.tva_normale_encaissement",
    "l10n_fr.tva_intermediaire_encaissement",
    "l10n_fr.tva_reduite_encaissement",
    "l10n_fr.tva_super_reduite_encaissement",
    "l10n_fr.tva_normale_encaissement_ttc",
    "l10n_fr.tva_intermediaire_encaissement_ttc",
    "l10n_fr.tva_reduite_encaissement_ttc",
    "l10n_fr.tva_super_reduite_encaissement_ttc",
    "l10n_fr.tva_sale_service_0",
    "l10n_fr.tva_sale_service_export_0",
    "l10n_fr.tva_sale_service_intra_0",
    "l10n_fr.tva_intra_specifique_biens",
    "l10n_fr.tva_intra_specifique_services",
    "l10n_fr.tva_intra_intermediaire_biens",
    "l10n_fr.tva_intra_intermediaire_services",
    "l10n_fr.tva_intra_reduite_biens",
    "l10n_fr.tva_intra_reduite_services",
    "l10n_fr.tva_intra_super_reduite_biens",
    "l10n_fr.tva_intra_super_reduite_services",
]


def _vn_coa_rename_xml_id(env):
    """
    Since the removal of account.chart.template
    we need to rename some xml_id like tax or tax.group
    in order to avoid duplication
    """
    env.cr.execute("""SELECT id FROM res_company WHERE chart_template = 'fr'""")
    xmlids_renames = []
    company_ids = [r[0] for r in env.cr.fetchall()]
    for company_id in company_ids:
        for tax_group_xmlid in _account_tax_group_xmlid:
            old_xmlid = f"l10n_fr.{company_id}_" + tax_group_xmlid.split(".")[1]
            new_xmlid = f"account.{company_id}_" + tax_group_xmlid.split(".")[1]
            xmlids_renames.append((old_xmlid, new_xmlid))
        for tax_xmlid in _account_tax_xmlid:
            old_xmlid = f"l10n_fr.{company_id}_" + tax_xmlid.split(".")[1]
            new_xmlid = f"account.{company_id}_" + tax_xmlid.split(".")[1]
            xmlids_renames.append((old_xmlid, new_xmlid))
    openupgrade.rename_xmlids(env.cr, xmlids_renames)


@openupgrade.migrate()
def migrate(env, version):
    _vn_coa_rename_xml_id(env)
    # # https://github.com/odoo/odoo/commit/f639de48eaee991b37bbaf8c62aecc4f425ea5e2
    # openupgrade.rename_xmlids(
    #     env.cr,
    #     [
    #         (
    #             "l10n_fr_viin.account_tax_report_line_purchase_val_exemption",
    #             "l10n_fr.account_tax_report_line_04_02_01_vn",
    #         ),
    #         (
    #             "l10n_fr_viin.account_tax_report_line_sale_val_exemption",
    #             "l10n_fr.account_tax_report_line_04_02_02_vn",
    #         ),
    #         (
    #             "l10n_fr_viin.account_tax_report_line_purchase_val_exemption_tag",
    #             "l10n_fr.account_tax_report_line_04_02_01_vn_tag",
    #         ),
    #         (
    #             "l10n_fr_viin.account_tax_report_line_sale_val_exemption_tag",
    #             "l10n_fr.account_tax_report_line_04_02_02_vn_tag",
    #         ),
    #     ],
    # )