# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RCountrycode(RPackage):
    """Convert Country Names and Country Codes.

    Countrycode standardizes country names, converts them into ~40 different
    coding schemes, and assigns region descriptors."""

    cran = "countrycode"

    version('1.3.0', sha256='34361416e771ece1d56dc56f79416c8b7f9591885773becae270684d095bc70f')
    version('1.2.0', sha256='32c65702dcc33d512ff99f14c12f4e0c48fe7ed7c8aa2f0a64194576d129dd40')

    depends_on('r@2.10:', type=('build', 'run'))
