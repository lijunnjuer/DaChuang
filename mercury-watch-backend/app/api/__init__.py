from flask import Flask
from flask_restful import Api

from .species import SpeciesListResource, SpeciesDetailResource, SpeciesSearchResource, SpeciesCategoriesResource
from .mercury import MercuryByRegionResource, MercuryBySpeciesResource, MercuryCompareResource, MercuryTemporalSpatialResource
from .region import RegionListResource
from .analysis import BiomagnificationResource, YearlyStatsResource, RegionRankingResource, ExportResource
from .report import ReportGenerateResource, ReportStatusResource, ReportDownloadResource
from .admin import AdminPingResource


def register_routes(app: Flask):
    api = Api(app, prefix="/api/v1")

    api.add_resource(SpeciesListResource, "/species")
    api.add_resource(SpeciesDetailResource, "/species/<int:species_id>")
    api.add_resource(SpeciesSearchResource, "/species/search")
    api.add_resource(SpeciesCategoriesResource, "/species/categories")

    api.add_resource(MercuryByRegionResource, "/mercury/by-region")
    api.add_resource(MercuryBySpeciesResource, "/mercury/by-species/<int:species_id>")
    api.add_resource(MercuryCompareResource, "/mercury/compare")
    api.add_resource(MercuryTemporalSpatialResource, "/mercury/temporal-spatial")

    api.add_resource(RegionListResource, "/region")

    api.add_resource(BiomagnificationResource, "/analysis/biomagnification")
    api.add_resource(YearlyStatsResource, "/analysis/yearly-stats")
    api.add_resource(RegionRankingResource, "/analysis/region-ranking")
    api.add_resource(ExportResource, "/analysis/export")

    api.add_resource(ReportGenerateResource, "/report/generate")
    api.add_resource(ReportStatusResource, "/report/status/<string:task_id>")
    api.add_resource(ReportDownloadResource, "/report/download/<string:file_id>")

    api.add_resource(AdminPingResource, "/admin/ping")
