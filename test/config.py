config = [
    {
        'path': 1,
        'description': 'Memasuki aplikasi, lalu memilih keluar aplikasi',
        'actions': [
            {
                'main-menu': 'Quit',
            },
        ],
    },
    {
        'path': 2,
        'description': 'Memasuki aplikasi, lalu menambahkan nama peserta',
        'actions': [
            {
                'main-menu': 'Make new participants',
                'full-name': 'AA'
            },
        ],
    },
    {
        'path': 3,
        'description': 'Memasuki aplikasi, lalu memilih untuk mengedit peserta, lalu memilih untuk keluar dari menu pengeditan',
        'actions': [
            {
                'main-menu': 'Make new participants',
                'full-name': 'AA'
            },
            {
                'main-menu': 'Edit participants',
                'target-name': 'AA',
                'edit-menu': 'Back',
            },
        ],
    },
    {
        'path': 4,
        'description': 'Memasuki aplikasi, lalu memilih untuk mengedit peserta, lalu memilih untuk mengubah nama peserta, lalu memilih untuk keluar dari menu pengeditan',
        'actions': [
            {
                'main-menu': 'Make new participants',
                'full-name': 'AA'
            },
            {
                'main-menu': 'Edit participants',
                'target-name': 'AA',
                'edit-menu': 'Edit name',
                'full-name': 'BB',
            },
        ],
    },
    {
        'path': 5,
        'description': 'Memasuki aplikasi, lalu memilih untuk mengedit peserta, lalu memilih untuk menghapus peserta, lalu memilih untuk keluar dari menu pengeditan',
        'actions': [
            {
                'main-menu': 'Make new participants',
                'full-name': 'AA'
            },
            {
                'main-menu': 'Edit participants',
                'target-name': 'AA',
                'edit-menu': 'Remove',
            },
        ],
    },
    {
        'path': 6,
        'description': 'Memasuki aplikasi, lalu memilih untuk pengundian secara acak, lalu memilih untuk keluar dari menu pengundian',
        'actions': [
            {
                'main-menu': 'Make new participants',
                'full-name': 'AA'
            },
            {
                'main-menu': 'Make new participants',
                'full-name': 'BB'
            },
            {
                'main-menu': 'Make new participants',
                'full-name': 'CC'
            },
            {
                'main-menu': 'ROLL RANDOM!',
            },
        ],
    },
    {
        'path': 7,
        'description': 'Memasuki aplikasi, lalu memilih untuk pengundian secara acak, tetapi tidak ada peserta yang cukup, lalu memilih untuk keluar dari menu pengundian',
        'actions': [
            {
                'main-menu': 'ROLL RANDOM!',
            },
        ],
    },
]