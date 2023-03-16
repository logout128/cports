pkgname = "vulkan-tools"
pkgver = "1.3.243"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DGLSLANG_INSTALL_DIR=/usr", "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf", "glslang-progs"]
makedepends = [
    "vulkan-headers", "vulkan-loader", "libxkbcommon-devel", "libxcb-devel",
    "libxrandr-devel", "wayland-devel", "wayland-protocols", "linux-headers",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
sha256 = "fcef5cb042b4477bd6a0cabc8c01301306d6b437cb9ea707fc3bee4a1dd79e3f"
hardening = ["vis", "cfi"]
# no test suite
options = ["!cross", "!check"]
