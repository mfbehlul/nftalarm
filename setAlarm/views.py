from django.shortcuts import render

# Create your views here.

def set_alarm_view(request):
    text=request.GET
    collections_list=["Blockasset Legends-Muhammad Ali","Blockasset Legends-Wayne Rooney","Blockasset Legends-Michael Bisping","Blockasset Legends-Jonah Lomu","Blockasset Legends-Alexander Ovechkin"]
    attribute_dict={'Attribute count': [0, 1, 2, 3, 4, 5], 'Type': ['Alien', 'Purple', 'Dark', 'Brown', 'Skeleton', 'Solana', 'Orange', 'Zombie', 'Red'], 'Clothes': ['Green Smoking', 'Orange Shirt', 'Black Kimono', 'Sailor Vest', 'Brown Jacket', 'Green Shirt', 'Poncho', 'Purple Shirt', 'Military Vest', 'Orange Jacket', 'Blue Shirt', 'Cop Vest', 'Pirate Vest', 'Green Jacket', 'White Shirt', 'Biker Vest', 'Orange Kimono', 'Red Shirt', 'Diamond', 'Beige Smoking', 'Black Smoking', 'Roman Armor', 'None'], 'Ears': ['Silver Earring', 'Gold Earring', 'None'], 'Mouth': ['Cigarette', 'Pipe', 'Vape', 'Mask', 'None'], 'Eyes': ['Vr Glasses', 'Vipers', 'Solana Vipers', 'Cool Glasses', 'Gold Glasses', 'Yellow Glasses', 'Green Glasses', 'Laser Eyes', '3d Glasses', 'Purple Glasses', 'None'], 'Hat': ['Black Backwards Cap', 'Green Top Hat', 'Cop Hat', 'Orange Cap', 'Green Backwards Cap', 'Strawhat', 'Blue Backwards Cap', 'Angel Ring', 'Ninja Bandana', 'Military Helmet', 'Blue Cap', 'Mining Hat', 'White Headset', 'Red Cap', 'Thief Hat', 'None', 'Firefighter Hat', 'Horns', 'Green Cap', 'Black Top Hat', 'Pink Headset', 'Red Punk Hair', 'Space Warrior Hair', 'Protagonist White Hat', 'Sailor Cap', 'White Fedora 2', 'Orange Backwards Cap', 'Green Punk Hair', 'Roman Helmet', 'White Fedora 1', 'Black Cap', 'Flower', 'Black Fedora 1', 'Protagonist Black Hat', 'Viking Helmet', 'Crown', 'Black Fedora 2', 'Sombrero', 'Pirate Bandana', 'Green Beret', 'Red Beret', 'Blue Punk Hair', 'Cowboy Hat', 'Pirate Hat', 'Purple Backwards Cap', 'Solana Backwards Cap', 'Admiral Hat']}
    context={"data":collections_list}
    return render(request,"setAlarm.html",context)
