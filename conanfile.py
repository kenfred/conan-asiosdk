from conans import ConanFile, CMake, tools
import os

class AsiosdkConan(ConanFile):
    name = "AsioSDK"
    version = "2.3"
    license = "Steinberg ASIO Licensing Agreement"
    url = "http://github.com/kenfred/conan-asiosdk"
    description = "Audio Streaming Input Output Development Kit"
    settings = "os", "compiler", "build_type", "arch"

    def build_id(self):
        # There is a single zip file for all configurations, so we only need one build variant
        self.info_build.settings.os = "Any"
        self.info_build.settings.compiler = "Any"
        self.info_build.settings.build_type = "Any"
        self.info_build.settings.arch = "Any"

    def package_id(self):
        # There is a single zip file for all configurations, so we only need one build variant
        self.info.settings.os = "Any"
        self.info.settings.compiler = "Any"
        self.info.settings.build_type = "Any"
        self.info.settings.arch = "Any"

    def build(self):
        # We don't actually build, we only retrieve sources
        # This could also be on in "source", but it would copy
        # to a build dir, and no need to have two copies.
        zip_name = "asiosdk%s.zip" % self.version
        url = "http://www.steinberg.net/sdk_downloads/%s" % zip_name
        self.output.info("Downloading %s..." % url)
        tools.download(url, zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.h", keep_path=True)
        self.copy("*.cpp", keep_path=True)