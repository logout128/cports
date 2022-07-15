pkgname = "dinit-userservd"
pkgver = "0.1.0_git20220715"
_commit = "3e9f389ee979bd466b29260f1bea77960f1d2e0d"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "ad2aeee607f38c8d50d7b8cb4617acee22d6ba520920948c1c18ea9429017ce5"
