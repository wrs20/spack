# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RAcme(RPackage):
    """Algorithms for Calculating Microarray Enrichment (ACME).

       ACME (Algorithms for Calculating Microarray Enrichment) is a set of
       tools for analysing tiling array ChIP/chip, DNAse hypersensitivity, or
       other experiments that result in regions of the genome showing
       "enrichment". It does not rely on a specific array technology (although
       the array should be a "tiling" array), is very general (can be applied
       in experiments resulting in regions of enrichment), and is very
       insensitive to array noise or normalization methods. It is also very
       fast and can be applied on whole-genome tiling array experiments quite
       easily with enough memory."""

    bioc = "ACME"

    version('2.50.0', commit='d55a19a8c091e8ea5fd35041520107a7f7603e14')
    version('2.46.0', commit='68f45c9f7d34c28adf6a0fc4245fdf63881109de')
    version('2.40.0', commit='38499e512998d54d874a0bfdc173f4ba5de5f01a')
    version('2.38.0', commit='cd03196428e8adf62e84f25c4d4545429e2c908b')
    version('2.36.0', commit='39e056435b9775d35e7f7fc5446c2c3cafe15670')
    version('2.34.0', commit='1f53d43e420e245423fdf2711d0dcb345f829469')
    version('2.32.0', commit='76372255d7714a0c8128a11c028bf70214dac407')

    depends_on('r@2.10:', type=('build', 'run'))
    depends_on('r-biobase@2.5.5:', type=('build', 'run'))
    depends_on('r-biocgenerics', type=('build', 'run'))
