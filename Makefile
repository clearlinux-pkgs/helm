PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v3.5.3/helm-3.5.3.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-3.5.3.tar.xz ./

include ../common/Makefile.common
