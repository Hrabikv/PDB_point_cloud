# 1. About this project

# 1.1. Python dependencies

* Those dependencies must be installed with "pip" to run the project:
  * TODO

* Changes in PostGIS database:
  * ALTER TABLE public.pilsen
  ALTER COLUMN geometry
  TYPE geometry(Point, 4326)
  USING ST_Transform(geometry, 4326);

* Discretization:
  * pip install open3d
