PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v3.2.1/helm-3.2.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-3.2.0.tar.xz ./

include ../common/Makefile.common
