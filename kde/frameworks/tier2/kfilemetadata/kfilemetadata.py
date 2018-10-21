import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.patchToApply["5.41.0"] = [("0001-Check-for-Linux-instead-of-TagLib-and-avoid-building.patch", 1),
                                       ("0003-Fix-build-against-TagLib-1.11.patch", 1)]

        self.description = "A file metadata and text extraction library"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None

        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None

        # self.runtimeDependencies["qt-libs/poppler"] = None
        self.runtimeDependencies["libs/taglib"] = None
        self.runtimeDependencies["libs/exiv2"] = None
        self.runtimeDependencies["libs/xattr"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
