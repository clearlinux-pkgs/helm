PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v2.16.0/helm-2.16.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-2.16.0.tar.xz ./

include ../common/Makefile.common
