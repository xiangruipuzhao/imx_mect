export LC_ALL = C

# ###############################################################
#
# Build setup
#

# Version of the LTIB local file system skeleton package.
SKELL_LFS_VER := 1.18-2

TOOLCHAIN_FLAG := SOURCERY_GCC=1

# Export MECT_RFSDIR for use in Makefiles generated by qmake.
export MECT_RFSDIR = $(MECT_LTIB_RFSDIR)

MECT_LDIR := $(CURDIR)/localfs
MECT_SPECDIR := $(CURDIR)/rpm/SPECS

MECT_QMAKE = $(MECT_QT_INSTALL_DIR)/bin/qmake

MECT_SMP_FLAG := -j$(shell grep -c ^processor /proc/cpuinfo)

# Use ccache.
export PATH := /usr/lib/ccache:$(PATH)

# All build targets
MECT_ALL_TARGETS := \
	local_prepare \

ifneq ($(wildcard 4c_runtime/.*),)
endif

ifneq ($(wildcard factory_test/trunk/.*),)
MECT_ALL_TARGETS += factory_test
endif

ifneq ($(wildcard key_generator/trunk/.*),)
MECT_ALL_TARGETS += key_generator
endif

MECT_ALL_TARGETS += \
	localfs_rpm \

# All clean targets
MECT_CLEAN_TARGETS := \
	local_prepare_clean \

ifneq ($(wildcard factory_test/trunk/.*),)
MECT_CLEAN_TARGETS += factory_test_clean
endif

ifneq ($(wildcard key_generator/trunk/.*),)
MECT_CLEAN_TARGETS += key_generator_clean
endif

MECT_CLEAN_TARGETS += \
	localfs_rpm_clean \

MECT_LOCAL_SPECS := \
	local.spec \

ifneq ($(wildcard 4c_runtime/.*),)
endif

MECT_LOCAL_SPECS := $(MECT_LOCAL_SPECS:%=$(MECT_SPECDIR)/%)


# ###############################################################
#
# Setup/build/deploy all projects
#

.PHONY: all
all: $(MECT_ALL_TARGETS)



# ###############################################################
#
# local_prepare
#

.PHONY: local_prepare
local_prepare: local_prepare_clean local_prepare_build local_prepare_install

.PHONY: local_prepare_build
local_prepare_build:
	mkdir -p $(MECT_LDIR)

.PHONY: local_prepare_install
local_prepare_install:
	test -n "$(LOGNAME)"
	sudo rpm --nodeps --root $(MECT_LDIR) --dbpath /var/lib/rpm --prefix / --ignorearch -Uvh --define '_tmppath /tmp/rpm' $(MECT_RPMBASEDIR)/RPMS/arm/skell-lfs-$(SKELL_LFS_VER).arm.rpm
	sudo chown -R $(LOGNAME) $(MECT_LDIR)
	sudo rm -rf $(MECT_LDIR)/var/lib/rpm
	-sudo rmdir $(MECT_LDIR)/var/lib
	-sudo rmdir $(MECT_LDIR)/var

.PHONY: local_prepare_clean
local_prepare_clean:
	sudo rm -rf $(MECT_LDIR)

# ###############################################################
#
# Project splash
#

.PHONY: splash
splash: splash_clean splash_build splash_install

.PHONY: splash_build
splash_build: MECT_PRJDIR := $(CURDIR)/splash
splash_build:
	test -n "$(MECT_PRJDIR)"
	cd $(MECT_PRJDIR); $(MECT_QMAKE) -spec qws/linux-g++-mx
	$(MAKE) $(MECT_SMP_FLAG) -C $(MECT_PRJDIR)

.PHONY: splash_install
splash_install: MECT_PRJDIR := $(CURDIR)/splash
splash_install:
	test -n "$(MECT_PRJDIR)"
	install -D -m 0755 $(MECT_PRJDIR)/splash $(MECT_LDIR)/root/splash

.PHONY: splash_clean
splash_clean: MECT_PRJDIR := $(CURDIR)/splash
splash_clean:
	test -n "$(MECT_PRJDIR)"
	-test -d $(MECT_PRJDIR) && $(MAKE) -C $(MECT_PRJDIR) distclean

# ###############################################################
#
# Project cgic_work
#

.PHONY: cgic_work
cgic_work: cgic_work_clean cgic_work_build cgic_work_install

.PHONY: cgic_work_build
cgic_work_build: MECT_PRJDIR := $(CURDIR)/cgic_work
cgic_work_build:
	test -n "$(MECT_PRJDIR)"
	$(MAKE) $(MECT_SMP_FLAG) -C $(MECT_PRJDIR) $(MECT_TOOLCHAIN_FLAG)

.PHONY: cgic_work_install
cgic_work_install: MECT_PRJDIR := $(CURDIR)/cgic_work
cgic_work_install:
	test -n "$(MECT_PRJDIR)"
	$(MAKE) -C $(MECT_PRJDIR) $(MECT_TOOLCHAIN_FLAG) INSTALL_ROOT=$(MECT_LDIR) install

.PHONY: cgic_work_clean
cgic_work_clean: MECT_PRJDIR := $(CURDIR)/cgic_work
cgic_work_clean:
	test -n "$(MECT_PRJDIR)"
	-test -d $(MECT_PRJDIR) && $(MAKE) -C $(MECT_PRJDIR) $(MECT_TOOLCHAIN_FLAG) clobber

# ###############################################################
#
# Project ATCMcontrol_RunTimeSystem
#

.PHONY: ATCMcontrol_RunTimeSystem
ATCMcontrol_RunTimeSystem: ATCMcontrol_RunTimeSystem_clean ATCMcontrol_RunTimeSystem_build ATCMcontrol_RunTimeSystem_install

.PHONY: ATCMcontrol_RunTimeSystem_build
ATCMcontrol_RunTimeSystem_build: MECT_PRJDIR := $(CURDIR)/ATCMcontrol_RunTimeSystem
ATCMcontrol_RunTimeSystem_build:
	test -n "$(MECT_PRJDIR)"
	$(MAKE) -j1 -C $(MECT_PRJDIR) -f _fcrts.mak TARGET=4CPC DEBUG=0 PRODUCT="USE_CROSSTABLE" $(MECT_TOOLCHAIN_FLAG) MECT_ROOTFS='$(MECT_LTIB_RFSDIR)' MECT_CC_VERSION='$(MECT_CC_VERSION)' MECT_CC_DIRECTORY='$(MECT_CC_DIRECTORY)' MECT_CC_RADIX='$(MECT_CC_RADIX)' all

.PHONY: ATCMcontrol_RunTimeSystem_install
ATCMcontrol_RunTimeSystem_install: MECT_PRJDIR := $(CURDIR)/ATCMcontrol_RunTimeSystem
ATCMcontrol_RunTimeSystem_install:
	test -n "$(MECT_PRJDIR)"
	install -D -m 0755 $(MECT_PRJDIR)/bin/fcrts $(MECT_LDIR)/root/fcrts.ATCMcontrol_RunTimeSystem

.PHONY: ATCMcontrol_RunTimeSystem_clean
ATCMcontrol_RunTimeSystem_clean: MECT_PRJDIR := $(CURDIR)/ATCMcontrol_RunTimeSystem
ATCMcontrol_RunTimeSystem_clean:
	test -n "$(MECT_PRJDIR)"
	-test -d $(MECT_PRJDIR) && $(MAKE) -j1 -C $(MECT_PRJDIR) -f _fcrts.mak TARGET=4CPC DEBUG=0 PRODUCT="USE_CROSSTABLE" $(MECT_TOOLCHAIN_FLAG) MECT_ROOTFS='$(MECT_LTIB_RFSDIR)' MECT_CC_VERSION='$(MECT_CC_VERSION)' MECT_CC_DIRECTORY='$(MECT_CC_DIRECTORY)' MECT_CC_RADIX='$(MECT_CC_RADIX)' clobber

# ###############################################################
#
# Project 4c_runtime
#

.PHONY: 4c_runtime
4c_runtime: 4c_runtime_clean 4c_runtime_build 4c_runtime_install

.PHONY: 4c_runtime_build
4c_runtime_build: MECT_PRJDIR := $(CURDIR)/4c_runtime
4c_runtime_build:
	test -n "$(MECT_PRJDIR)"
	$(MAKE) -j1 -C $(MECT_PRJDIR) -f _fcrts.mak TARGET=4CPC DEBUG=0 PRODUCT="USE_CROSSTABLE" $(MECT_TOOLCHAIN_FLAG) MECT_ROOTFS='$(MECT_LTIB_RFSDIR)' MECT_CC_VERSION='$(MECT_CC_VERSION)' MECT_CC_DIRECTORY='$(MECT_CC_DIRECTORY)' MECT_CC_RADIX='$(MECT_CC_RADIX)' all

.PHONY: 4c_runtime_install
4c_runtime_install: MECT_PRJDIR := $(CURDIR)/4c_runtime
4c_runtime_install:
	test -n "$(MECT_PRJDIR)"
	install -D -m 0755 $(MECT_PRJDIR)/bin/fcrts $(MECT_LDIR)/root/fcrts.4c_runtime

.PHONY: 4c_runtime_clean
4c_runtime_clean: MECT_PRJDIR := $(CURDIR)/4c_runtime
4c_runtime_clean:
	test -n "$(MECT_PRJDIR)"
	-test -d $(MECT_PRJDIR) && $(MAKE) -j1 -C $(MECT_PRJDIR) -f _fcrts.mak TARGET=4CPC DEBUG=0 PRODUCT="USE_CROSSTABLE" $(MECT_TOOLCHAIN_FLAG) MECT_ROOTFS='$(MECT_LTIB_RFSDIR)' MECT_CC_VERSION='$(MECT_CC_VERSION)' MECT_CC_DIRECTORY='$(MECT_CC_DIRECTORY)' MECT_CC_RADIX='$(MECT_CC_RADIX)' clobber

# ###############################################################
#
# localfs_rpm
#

.PHONY: localfs_rpm
localfs_rpm: localfs_rpm_clean localfs_rpm_build localfs_rpm_install

.PHONY: localfs_rpm_build
localfs_rpm_build: MECT_PRJDIR := $(CURDIR)
localfs_rpm_build:
	test -n "$(MECT_PRJDIR)"

.PHONY: localfs_rpm_install
localfs_rpm_install: MECT_PRJDIR := $(CURDIR)
localfs_rpm_install:
	test -n "$(MECT_PRJDIR)"
	test -n "$(MECT_TMPRPMDIR)"
	tar cjvf $(MECT_RPMBASEDIR)/SOURCES/local.tar.bz2 --exclude=.svn -C $(MECT_LDIR) .
	mkdir -p $(MECT_TMPRPMDIR)
	rm -rf $(MECT_TMPRPMDIR)/{*,.??*}
	for s in $(MECT_LOCAL_SPECS); do \
		rpmbuild --define '_topdir $(MECT_RPMBASEDIR)' --dbpath $(MECT_TMPRPMDIR)/rpmdb --target arm --define '_target_cpu arm' --define '_arch arm' --define '_prefix /' --define '_rpmdir $(MECT_RPMBASEDIR)/RPMS' -bb --clean $$s; \
	done

.PHONY: localfs_rpm_clean
localfs_rpm_clean: MECT_PRJDIR := $(CURDIR)
localfs_rpm_clean:
	test -n "$(MECT_PRJDIR)"

# ###############################################################
#
# Project factory_test
#

ifneq ($(wildcard factory_test/trunk/.*),)

.PHONY: factory_test
factory_test: factory_test_clean factory_test_build factory_test_install

.PHONY: factory_test_build
factory_test_build: MECT_PRJDIR := $(CURDIR)/factory_test/trunk
factory_test_build:
	test -n "$(MECT_PRJDIR)"
	cd $(MECT_PRJDIR); $(MECT_QMAKE) -spec qws/linux-g++-mx -config codesourcery
	$(MAKE) $(MECT_SMP_FLAG) -C $(MECT_PRJDIR)

.PHONY: factory_test_install
factory_test_install: MECT_PRJDIR := $(CURDIR)/factory_test/trunk
factory_test_install:
	test -n "$(MECT_PRJDIR)"
	install -D -m 755 $(MECT_PRJDIR)/factory_test $(MECT_LDIR)/root/factory_test

.PHONY: factory_test_clean
factory_test_clean: MECT_PRJDIR := $(CURDIR)/factory_test/trunk
factory_test_clean:
	test -n "$(MECT_PRJDIR)"
	-make -C $(MECT_PRJDIR) distclean
	make -C $(MECT_PRJDIR)/trama $(MECT_TOOLCHAIN_FLAG) distclean

endif

# ###############################################################
#
# Project key_generator
#

ifneq ($(wildcard key_generator/trunk/.*),)

.PHONY: key_generator
key_generator: key_generator_clean key_generator_build key_generator_install

.PHONY: key_generator_build
key_generator_build: MECT_PRJDIR := $(CURDIR)/key_generator/trunk
key_generator_build:
	test -n "$(MECT_PRJDIR)"
	cd $(MECT_PRJDIR); $(MECT_QMAKE) -spec qws/linux-g++-mx
	make $(MECT_SMP_FLAG) -C $(MECT_PRJDIR)

.PHONY: key_generator_install
key_generator_install: MECT_PRJDIR := $(CURDIR)/key_generator/trunk
key_generator_install:
	test -n "$(MECT_PRJDIR)"
	install -D -m 755 $(MECT_PRJDIR)/keyGenerator $(MECT_LDIR)/root/key_generator

.PHONY: key_generator_clean
key_generator_clean: MECT_PRJDIR := $(CURDIR)/key_generator/trunk
key_generator_clean:
	test -n "$(MECT_PRJDIR)"
	-make -C $(MECT_PRJDIR) distclean

endif



# ###############################################################
#
# Utilities
#

.PHONY: clean
clean: $(MECT_CLEAN_TARGETS)
