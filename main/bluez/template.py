pkgname = "bluez"
pkgver = "5.70"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-systemd",
    "--disable-experimental",
    "--disable-deprecated",
    "--disable-mesh",
    "--disable-nfc",
    "--enable-cups",
    "--enable-sixaxis",
    "--enable-threads",
    "--enable-library",
    "--with-udevdir=/usr/lib/udev",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "flex",
    "python-docutils",
    "automake",
    "libtool",
]
# TODO: look into porting to libedit later
# same story as iwd, really crappy usage of readline API
makedepends = [
    "udev-devel",
    "dbus-devel",
    "cups-devel",
    "glib-devel",
    "libical-devel",
    "readline-devel",
    "linux-headers",
    "musl-bsd-headers",
]
pkgdesc = "Linux Bluetooth stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/{pkgname}-{pkgver}.tar.xz"
sha256 = "37e372e916955e144cb882f888e4be40898f10ae3b7c213ddcdd55ee9c009278"
tool_flags = {"CFLAGS": ["-Wno-deprecated-declarations"]}
options = ["linkundefver"]
system_groups = ["bluetooth"]


def post_patch(self):
    self.mv(
        "obexd/src/org.bluez.obex.service",
        "obexd/src/org.bluez.obex.service.in",
    )


def post_install(self):
    self.install_file("src/main.conf", "etc/bluetooth")
    self.install_service(self.files_path / "bluetoothd")


@subpackage("libbluetooth")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("bluez-devel")
def _devel(self):
    return self.default_devel()


@subpackage("bluez-cups")
def _cups(self):
    self.pkgdesc = "CUPS printer backend for Bluetooth printers"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cups"]

    return ["usr/lib/cups/backend/bluetooth"]
