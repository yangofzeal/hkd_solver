# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('3516ab1a465aa83657f59ee2cf474e60c46c4f947e40c78747ff4b1742a6f057afcc7a52540109b10d9b6d0fd918c3bb5ef3800a1994c1568329beb28915ed94fc1af0eba2b0e86082a5ce4ab7b5232b2d9636880211c0452e229172f42aee8ac996ade9a8a36599e4fe949997c7f75d62a2ee34e0ad173d9b595b17fce46ab0'),
        _hb.unhexlify('a331b25ba730b2362dbc059af25f79aaa32638ef3613715525b4fd4944bec7d16650ae9a19e53917b9c5eb75e0a7064cc483e5c39410d057528ed01db8ecb8db9d3c0a44a6742a52ed4dafd113761aec626ddb8de56b2c58e9f2d63986f8a3faf6bb2b87941b6d4d7700ee19b42cb2a728eabef5df02944b0d4a80c52d1e36d0'),
        _hb.unhexlify('4ac18823b0f438193e9e1179617e65fdbca36c6250692f1ce5fcbb459c7b6721850ca4c0d2b49a3583c8579daf39c6b030629e6deb49e51a46baa9f4a6d063a88be81aeb081d6bc64d512175721d3a588a7c4790739c500f144ea1fe8c23c66316fd8c07841bc28ce45de9a5f56355b9db38cc2cfef1627c24f8dda31a5b79ac'),
        _hb.unhexlify('fa6167426fb0be87e37d11ff293253eb2cd3ee5ba367c5a160d8af32d087d88597c00922d52851ebd8260e476e36c62bc090bcacda801617e47388c3e9e0dd90c21d0c30cd4efedb202e536f958e85c37adda5127a4adb56c93e478b08c027e8a3366f90094fbf965683b9fe0d1682324e0ae7b3fd1f5f831a71a7bd4042f294'),
        _hb.unhexlify('2eae2a425ba297037aa94aa26f06b358891c7892e21bc3a3ea16aab352e3367c412b26d2e9288e09c10cde8795b98068bccf2e49c30bb9ab574e0eb308a02cda299b653d13ef79aeb07dec86901313072cbdd13d68b13d83187c5892d983599f080cc574ee46c7cf869b3f0c15152794deb5d64e91a2fada4e87b48555cd019f'),
        _hb.unhexlify('49f21876c4e304c39082daa8dc33284587a2208983d519ad34ee07ab39b6f1756897aae3a2cd9df116aa5513c1873af5d00ba1fbbc9edc83d864b14c84ec3102ea1b8cfddaac80beb663cb450050c61c869af276c417eb0c643f156cdf7d7b363e8498706e44ea1f19856deeced19aa893c5fdf82bb5d5f88a80ebc38877f6d8'),
        _hb.unhexlify('e4ce34a4c8b8f3fa243c20bb6312d1a1084239f74f016e32f357ea2e70b46e3ce249bc305345c02eb0bfab1496c5fdab385a8b211e8b9c0bdf4a5f80f99889fc1885119bd0bbbd4d50196051d51fbc25044110b54c4689c46e4f9806c3627333be883a43cb39638b553ceb5498415f98c3a5b2429887241faa8e4c66fc97b147'),
        _hb.unhexlify('06149417f079fcdd04e00f591ce49364e276642195cf515ff8cae2f8dc1f4aae394c5a54d22f5db7e4d3ea299d118cda622e24caca946374bcf9f5b713b52f107f68851ea6f35cbd1c52cb02936bf0625c81b6eeadbe1e6600c8999c46521f0ed3afe408cfee09bf1ccb31f184840e156ad76feb72ff1b8a3dfb05085fe3f855'),
        _hb.unhexlify('96a31af14c8ce644d7cbc497392b1bfe2feb93b9ea4a8ecea2b3f7ed09da043cc324a2d762f51a8ddf0de7b9161ada4f20f358bd954620a4a8c72260cc1f68af6de9b9454ef9a5f1301af3c81ca411c401b5f30c6f99e7e2b9cb4e5108f5a8494f4ba4128f4badcf37be8bbb57e063a7584378e36b440aa3601619a5fce008ee'),
        _hb.unhexlify('cefa7da7b85692bf6c8bca25885b971588ed9a597c55bd9bb7250620f217029ecce5b825cabd7b771cd3e9d213b7019e1577092cf3c7fe001cccf6444cc5ae4c3aba992d76c04c620d8181aae00a9331de9dc009060623303ecea18cda25361394cdb46bc1c9388ee67bab4fa8753a9e664171f9f72d51d0db314bb09bd22cd8'),
        _hb.unhexlify('26f69c54021f4cc16f58df0549670414291d08c220a76fc5fcc9400afef03ca4b98391430328c895c10d5bff81320d6261c8eb912da88abff83477e3ecae5c41315a9831eebd3ad7130479538a41ccd60b4f42ba17f6f7cc399c8499b901c4fed1bddeb40333d9b3dfd5c641f1492687541805954658b238bb749c7be4c7a74e'),
        _hb.unhexlify('fb83512363f0e5c1f3a96e92b1b3faf126d571e68fc56b531f19c018605e3bed5c56bd5152b1901222c614b4dc3c5801c9c379ea74517bf88bc9a039e9174c2d67f0ca2ce6bd65aec4f0315ac7a7806d341ff05c284c1df5480a4fcae5dde2df7a232d940e00fdff507ada81f51e4f09699f9128b42939085e458cb5e7cd1910'),
        _hb.unhexlify('aa725d665696d8477ab23df061bd9c0079a4ba7016b4cc61938442efbcc301393c46665f0026351bfdcc06410013658e15dfad5ed524aff1e217bad12b39756411525f588b5d6022d1fff648cdb3d09f58963bd82a1c7f13d08f1d28be448e3e4ab76f5853e47b033228683a205104131b338e0a77377548b633e2ff4e638bbd'),
        _hb.unhexlify('770a6b848d8cacf032691f63f8aff213bba721233ed192a54e246dc81c9a880dd2b8c592ca0a02ca2d96b7cf0087922dc3d90985d59e1d7cb54297597cc0cfb938ad9b9d02108f81e43541204cf1fcd4403fe070ada30ed6a3a0e9aa14a40d2ca2eaedc3ee58d00d7afc8b9406aa2616689f1a064c302b4f869b0a577d9ceb29'),
        _hb.unhexlify('d17b88c710101a2e86529abdaddac02f530c21ee8593026a4e19fa7835314968ce8f80ed20ca2acb89b3f75e7b11271f6dc8781848a2811491017664f6702a444707c07dfcf0b78ebe3a3fc0715540ff2bfab9f95a207f8a99092c6b54bb7c2c310af99ec834b48e7a9bcc09dde6ee702011b6544d3e751ef175ddfb36e20cbe'),
        _hb.unhexlify('f35f5adcb10eb06eeb80915098df315956ea61c54388ad6c3f184a422e353a917bdf5adfaa7b5966f20ca3f05511ab31980e2a57b5de06d80b647096a5a116354cd3aaf5c977928b01986138948cd22070ba5bb9be7fd4e484ef00ce3b217e91cb43b501bc7686907cd5ead27c7b2c9ac95c87e376e5a53917a98ce2e3b7bd38'),
        _hb.unhexlify('7d85906f8f111dca9e770061c9191f33f0f57ab6da63dcd443e423b502a6dfbfd103c40955bbc6438f291a7c2e34803839c2d149355bd36d30cbaf0d06e53ff97e4592ef5e7b23579cd71fd785892796040a1f9ed72640bad4c7b7a32c3437561b52dd84acff66fa8642738b74b986ea858ffef39038ffc1648718584d7fc881'),
        _hb.unhexlify('92195e16e74e53357372e5a9a47d1b1988fe5eb1f56bd7c1e62ea65047e1cd36324cd40dc39b9f3a609a11ed0d3d1e4b30b933f36d49bcb8d6eef1c6abf8dcf763852c18fc09b1566d3429116722e5c71618777f05f1cc6cc384ff1a15066f3b9c1e3116d8c4f23f33b88d7a84a14b8a6b0cb44f9a2865a0bef46331c28362a0'),
        _hb.unhexlify('47ecd77478bd3d4a9692f63545ad9f6cdf413a0ba35222835b6e83f941a64f9ab92099c363d7bbe2c3bd1ca9348bb4400384c9ff46ce66965df0e40f6c90d45ed8feb691e45cb26b8e6eedbe8d9678b8ec5f55a42fcc283e7f9ccd1fa4ab4f89c6e7e51f0a7c24bc2b1d81b5d6a1a4a40a9d79b2c77346d3bdc5226b657f3876'),
        _hb.unhexlify('35e5ddfb80b6351523ce2b62be85f84c23aed8012f9ae71ad17619aca8835b4fefbf9127d106b429d5832a7057a7679854ebf8f288c1366e9dfd246736f1373b93205dabbe8c3e7d1e3e5ffb13fd9740346d2c543bf1b731ef8eea24a67ad545ffa7486d52228bb91d2507d13811b28fd07d10efa9bfc9eac2a339f0ec069cad'),
        _hb.unhexlify('a50ba80cae8c583564e7db10edc273b82bd78b6a8872d0bdfd4d646da15919c5be2bcddb8655c6481d026b2f93949cf350f2b473c2d49b7ff932b3b340ad2b90a654e1c10498739cee1d33debcc9bf85c3c5e26c9273e38efadc1f4355ed40f8f5825368140dca3cf1dc61129e32da392c68d791cb6826e6b224adbcb63d30a9'),
        _hb.unhexlify('b03ed3db0639628ff3e3fd822b88e8b0e9f6f3c85cbc35e551decd51507e6839a25bb9651b8c00e89db598383f054db697251d67b138a6772410dfa85160aa24e6b06313eb675d261a305450893b64a48bebe8d40c10dc46782c83c9eb754aa9ab1336d3ccab84a12644e332fb378e8315471efba1e6baffa389ef1d71a6102c'),
        _hb.unhexlify('a1a6cf91d105f700427ad33edcf6f495a1b0506f39486d524b2e0d5c8536479bcb9c27444329f6c9e3fcacc4147bde2770d29fd93924a9c02e01ab64bbce7a2800530367089b91ef681ebf4cc870c8e852a5a915a0a009d41701a597159ebf145ef0308fd14468ecfaccf43d1eb826ddb4394d3b2f971bafae0130fb77938b86'),
        _hb.unhexlify('5caabb200b9a243f45f30257864c7b5edf73f997e7964c778f7d2073ecaec918af4158dcd25f00dd4cca8df1a421d96e1a5393fe80559955005d72a9815b889b8c0be0d5eb602b06c5fdefaf6836e277bf11e242c1ccc197bf0fd49abfb73bd91c7fccef3d2881dde88b266cdce9d7d89af24cd720cb97feaefde889868774a7'),
        _hb.unhexlify('11707ced6685063cbf8678e548e0832f164c98d102a16777a4a9564120ff682b5e3478a56da12c518273b9ac3822c742a613d92119e0abc28f9bec41c12ee53f656a5f7f3935ecc120d7b060aace26a866d7dc7c85cde7a3c83a93a6c296bdcc0883abbd33676d8eebdc366e63bebab4bde803fd933d9106ea0da5362c71cff7'),
        _hb.unhexlify('8fc9f84e4cecbbab6bc87cec7dfd82b4f79962688dca7da80813d5bc52267e9513cd00864ba7b32890f3a0e378'),
        _hb.unhexlify('2325c60a6329d285b69a7de41e45c3b4049fc46a75409f0e54783639a3c58e2fbbbefb32ba3165ec11806e1dfd697f1a3e1be8dd2169886937aff31cb3248bd776d56b015a4f3f356dbb74f4eedb51928f8f0f7a5496238ff869433df100b2dbe8d2fa285a0118dba4817d6effe86a88e9151b7cbb64f35774570202f35517ad'),
        _hb.unhexlify('8287340c3b42b51033a5ed2fb970ec417f35702ce0e12e76c2168d0ac3bdd68e359c7877f6b86e16b0ab5e4637b1b72dba003544c5208c1954a523c9164ff016ca0be13e1b917e64647a72fbb333cac8065dce25282633d410ea7a527a8ee5a14e8bcbbe1e893b039f745f1223a8d34a24ff59c90070bbbd4780f1c59c88d1fb'),
        _hb.unhexlify('9cd7246240537a11502ceaa0d4b28b8c23e31b016b396ff36f53d28603d31048d2f6b23d1e7c14749a0cb463a1a4f0fa11734fed017901d92e5169ea39c3caa4c03cc7c1fae97720830318ac7ede61c8622f0f62283b58dbcc0cf55b7e1309a1bcc21b99b56ee0dfd9913af099880af03b0ffd0e0939fd7f90828680de622f00'),
        _hb.unhexlify('16b5ed243db926ccc6ed5f3e8e6d6d33c08c3c973df3bb918ba0c56de25bb3c04fc8909714a280283f79f0123a066432f143f9c30a81345627ec92b11725dd7a83e39c23e844e815a1fe9e0498b275c5db16f8ad36f0b36d32ed71c68af623eb7add2e85d6fec9b7b8d219fe6a2b44d692f107ac23aefeef724cf6242035b872'),
        _hb.unhexlify('ed99b0954e0458f01a2435d4d7df8b2b4c1b3ad92d2565ec96024b095b48fbe741933102fb7ff787e27ec3247989f1ac6db13cf01fdcd0ef150aeb0c9f2419a0133d9864af3479caa8a74d23f93731e7de08d6322d89fd1c5b76377984eb4c0c3dc3ad92c2df9466595f547318c6518d703b4aa525a9eca3e3c4c1363b9d8f0b'),
        _hb.unhexlify('a7060515e854f256f3a04aa51031003cd27e14d04660f0c26c7373e4e9451d50261a51599e3d5791d2cec252c30e13a37bc7d28f28c1c2f0cc72f9f1109a189a299106f163593afcaf36a9dcd6d363496cc9b65fc553fec2a617f5a505b97dbb5a0b974f7134236b3b98be68d9223f8741e3951614e70f220250d670471be3ed'),
        _hb.unhexlify('01fe9eddfe436196cbc91417561a34c5ecf1c5987ad6d9c21e635887e4d7208cfb3fcaff90febf2ac4b65e18fffae30827986479dc2e64347dbd4033d60295cb6f3fc43ccb6ec0779d13d8f9d1b35a3f23a21be78f1dfe6d1d2a3b6629b0233a7b6c29f65e6fa10bd1c51b78833dfad186f903c50c0df38df0ad8ee1b4392c49'),
    )
    _inv = (12, 20, 17, 29, 24, 2, 6, 14, 4, 18, 0, 26, 28, 8, 3, 22, 16, 5, 1, 27, 31, 9, 21, 13, 15, 11, 23, 19, 10, 30, 32, 7, 25)
    _leaves = (
        _hb.unhexlify('8e2081339901c72283a4256db6d892fa1fcd54945c5dd6149464dc0600b93eca'),
        _hb.unhexlify('8eb10b7ed9fb879f4066a4a992efed9e02a2e256ef5296fd8062177a29fd014a'),
        _hb.unhexlify('cb6987b584f0e5362616db1b0edafc2a320b692ef240fcbb91cdeaf8ceadfc92'),
        _hb.unhexlify('4a2e1ebf935d820d6e35833f3def6ee70ddfa254ab49d7af7b8d798f2a479bb8'),
        _hb.unhexlify('391f35c9839d54152aadf017497e7c6885d8c3ded18a8bba59218367c1e475da'),
        _hb.unhexlify('d17c0e060d4e4bdc99c9a202fd4260b8abbc82961f52c75e44920288a9a0215c'),
        _hb.unhexlify('78a0f0b66b62df449e8df1c06231227c8b661fa24464fdad789dfdc0f921a399'),
        _hb.unhexlify('25f36070e51d4b1d816b2f1dd98181941b9f2b0d94f0ad0df03289aeb8845c9b'),
        _hb.unhexlify('9a77676afd17bce72a29ba699f0a4ca189eb7ebb8b677b23f657c23287258588'),
        _hb.unhexlify('7af0c6a876b6ff53a9c1e7ceeea28ac243f62b2598c23e0243224bf8ab9d349b'),
        _hb.unhexlify('624ce8a823158cc1e8d1614b1737a99b456cb55deedee361070145f75686b6cb'),
        _hb.unhexlify('e074356647e14e8e7a8638c2ee11dad596a8ea46ff7df6c5bf1fff547ec77a18'),
        _hb.unhexlify('b6e17265f347659a03a0deeb3f90016ac4f9cf981d978e8a819c41fd93a923b0'),
        _hb.unhexlify('29c8676285ebc7624f2c34f33176011a717a24c7079ae82ac418697299964cd6'),
        _hb.unhexlify('03df269eed3da37ac40fb8c7c35233c5012d31cef8f0a4776355789ab27c89c0'),
        _hb.unhexlify('7f4c6ac4fbb6c8761f781f806f64bc9c0084af4f3b16aa2c4370d2085cd0644e'),
        _hb.unhexlify('b663d4f7d719f18cef7260af8c0a30870c1fb37a3bf812267bcafadd9c88ebcf'),
        _hb.unhexlify('7d796dd32125065e37079a8b3269eac474fb7e3283cd576a3bb774d744ce55bf'),
        _hb.unhexlify('af9407bd6e4b51b1c40fa4955429032da9dceb2527f52565be25c14b281b6b6b'),
        _hb.unhexlify('953cd48b3d700a24b0e134e247454374739082fbd62f71b45966905ffcc180b9'),
        _hb.unhexlify('e7785021973cb7447427f67a8750e5ab2efc2f4b8ab241f1f4638a232d109919'),
        _hb.unhexlify('96e806b675e446abb6a7d54f90c652f4beffb656533c6fee78c1cff390002ec3'),
        _hb.unhexlify('06412a3b8e908447d809e161cf3e14a600218a5058bda0cc9845de75540aeca0'),
        _hb.unhexlify('4df48564039562dd8821892d052067916a1a7a916f6b3296fb9749f54aa9580e'),
        _hb.unhexlify('4dbd3190e48acbfef7331b010adab1b2d67745a1aa755d9730b63c075449ec5d'),
        _hb.unhexlify('005877068e180185c194197f94f147353be5c1cb97b62243ad52bba04833b81c'),
        _hb.unhexlify('fc9f4c7859d8c1060e993dbe27564063f8a4fdeed6c71ef71a8d0e4dcffa1c7c'),
        _hb.unhexlify('0ce904695208696a0965d0bf675110e1ac35ca8066522b1ff25d95e2f2fc3047'),
        _hb.unhexlify('e1ee58d5f8562d065cdb38f2b713ea943bb373f40553dca77fa355341af2b65a'),
        _hb.unhexlify('9ad51c413b8beadf34d84582fc3fc2292dd445a92a87719f8f5aadc6c495b37a'),
        _hb.unhexlify('406ccbcc5f788db7882be571361ce2e7a1c3a31f647bc5c980cd2ff9bfdbda04'),
        _hb.unhexlify('67b09f8ce8f9a8db06dab1cdd56c105d63a6f797e03363d23bb5358c9dcdf6d6'),
        _hb.unhexlify('c387a3236809d657b78742f8f77e5e7841a2239e6f3534487a7aa99b6912828d'),
    )
    _root = _hb.unhexlify('3923b83bbcb37a34acca208c2ed8e451e6eff180b8b1ea13be1574f1771d032a')
    _share1 = _hb.unhexlify('55eda5f163d89abc0fa9ee2f50360fb8a1798cbdee89b7724aa601d666ef165c')
    _share2 = _hb.unhexlify('9f79c9c5af812421529d38fa0edc11dc26853438e917cd18eb1ba098b56c4e3b')

    def _u32(_n):
        return _hs.pack('>I', _n)


    def _xor(_a, _c):
        _o = bytearray(len(_a))
        _i = 0
        while _i < len(_a):
            _o[_i] = _a[_i] ^ _c[_i]
            _i += 1
        return bytes(_o)

    def _ks(_key, _index, _length):
        _o = bytearray()
        _counter = 0
        _seed = _key + _u32(_index)
        while len(_o) < _length:
            _o.extend(_hh.sha256(_seed + _u32(_counter)).digest())
            _counter += 1
        return bytes(_o[:_length])

    def _merkle(_values):
        if not _values:
            return _hh.sha256(b'').digest()
        _level = list(_values)
        while len(_level) > 1:
            if len(_level) & 1:
                _level.append(_level[-1])
            _next = []
            _i = 0
            while _i < len(_level):
                _next.append(_hh.sha256(_level[_i] + _level[_i + 1]).digest())
                _i += 2
            _level = _next
        return _level[0]

    _key = _xor(_share1, _share2)
    _parts = []
    _verify = []
    _i = 0
    while _i < len(_inv):
        _masked = _b[_inv[_i]]
        _raw = _xor(_masked, _ks(_key, _i, len(_masked)))
        _parts.append(_raw)
        _verify.append(_hh.sha256(_u32(_i) + _raw).digest())
        _i += 1

    if tuple(_verify) != _leaves or _merkle(_verify) != _root:
        raise ImportError('HKD protected payload integrity verification failed')

    try:
        _source = _hz.decompress(b''.join(_parts)).decode('utf-8')
    except Exception as _exc:
        raise ImportError('HKD protected payload reconstruction failed: %s' % (_exc,))

    _filename = _g.get('__file__') or '<HKD-obfuscated>'
    _code = compile(_source, _filename, 'exec', 0, True, 0)

    # Discard the plaintext string before running user code.  CPython may reclaim
    # it immediately; no plaintext source is retained as a module global.
    del _source

    # Return the compiled payload.  Keep exec out of this function: older
    # CPython parsers reject an exec statement in a function that also contains
    # nested functions/free variables.  Execution happens at module scope below.
    return _code

_hkd_v4_code = _hkd_v4_bootstrap(globals())
del _hkd_v4_bootstrap

# Exact module semantics: execute in the real module globals.
exec(_hkd_v4_code, globals(), globals())
del _hkd_v4_code
