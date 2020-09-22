PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v3.3.4/helm-3.3.4.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-3.3.1.tar.xz ./

include ../common/Makefile.common
