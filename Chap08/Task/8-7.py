def make_album(artist_name, album_title):
    full_info = {'artist': artist_name, 'album': album_title}
    return full_info
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Adele', '25')
album3 = make_album('Ed Sheeran', 'Divide')

album_list = [album1, album2, album3]
for album in album_list:
    print(album)

def make_album(artist_name, album_title, song_numbers=None):
    if song_numbers:
        full_info = {'artist': artist_name, 'album': album_title, 'songs': song_numbers}
    else:
        full_info = {'artist': artist_name, 'album': album_title}
    return full_info
gaga = make_album('Lady Gaga', 'Chromatica', 16)
gem = make_album('G.E.M', 'City Zoo')
print(gaga)
print(gem)

def make_album(artist_name, album_name):
    """返回包含专辑信息的字典"""
    full_info = {'artist': artist_name, 'album': album_name}
    return full_info

while True:
    print("\n请输入专辑信息（输入'q'退出）")
    a_name = input("请输入歌手名称：")
    if a_name.lower() == 'q':
        break
    al_name = input("请输入专辑名称：")
    if al_name.lower() == 'q':
        break
    album = make_album(a_name, al_name)
    print(album)