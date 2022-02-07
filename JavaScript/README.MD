# JavaScriptNotlarım

## Değişken 
* Değişkenler en basit tabirle değerleri hafızada tutmak için kullanılan yapılardır.
* eğişken isimleri harf, _ veya $ işareti ile başlayabilir. ve bunu harici başka noktalama işareti kullanılmaz.

#### Var
* Değişken değerleri değiştirilebilir.
* Aynı isimle tekrardan tanımlanabilirler.
* var ile tanımlanan değişkenler global scope veya function scope'tur. Global scope'ta tanımlanan değişkenlere her yerden ulaşılabilir. Function içerisinde tanımlanan değişkenlere ise tanımlı olduğu fonksiyonda ulaşılabilir. Bu konuyu örneklerle açıklayalım.

#### Let
* Değişken değerleri değiştirilebilir.
* Aynı isimle tekrardan aynı blokta tanımlanamaz. Farklı block'larda aynı isimle tanımlanabilir.

#### Const
* Const ile tanımlanan objelerin özellikleri (properties) değiştirilebilir fakat objenin kendisi değiştirilemez. Diziler içinde aynısı geçerlidir. Dizi değerleri değiştirilebilir fakat dizinin kendisi değiştirilemez.

#### Hoisting 
* Yukarıya alınan değişkenler var ile deklare edildiyse atandıkları değer yerine undefined değerini alır. let veya const ile deklare edildi ise ReferanceError hatası verir. 

---
## Number Veri Türü Kullanımı, Temel Aritmetik İşlemler ve İşlem Önceliği ve Arttırma ve Azaltma İşlemleri
 
 * eğer ++ veya -- değişkenin önünde ise ilk önce toplar sonra değişkene ekler eğer sonunda ise ilk önce ekler sonra toplar.
---
 ## Boolean Veri Türü İle Çalışmak

 #### Örnek
``` JavaScript
b1 = Boolean(100);
b2 = Boolean(3.14);
b3 = Boolean(-15);
b4 = Boolean("Hello");
b5 = Boolean('false');
b6 = Boolean(1 + 7 + 3.14);
True
```
``` JavaScript 
c1 = Boolean(undefined);
c2 = Boolean(null);
c3 = Boolean("");
c4 = Boolean(false);
c5 = Boolean(NaN);
c6 = Boolean(0);
c6 = Boolean(-0);
False
```
---

## Değişken Türünü Kontrol Etmek

```JavaScript
console.log(typeof 42);
// beklenen output: "number"

//isInteger( ) yöntemi, sayıların tam sayı olup olmadığını belirler.
Number.isInteger(123) //true
Number.isInteger(-123) //true
Number.isInteger(0.5) //false

//isFinite () yöntemi, bir değerin sonlu bir sayı olup olmadığını belirler.
Number.isFinite(0) //true
Number.isFinite('123') //false
Number.isFinite('Hello') //false
Number.isFinite(-Infinity) //false
Number.isFinite(0 / 0) //false

// Number.isNaN () yöntemi, bir değerin NaN (Not-A-Number) olup olmadığını belirler.

Number.isNaN(123) //false
Number.isNaN(0) //false
Number.isNaN('123') //false
Number.isNaN('Hello') //false
Number.isNaN('') //false
Number.isNaN(true) //false
Number.isNaN(undefined) //false
Number.isNaN('NaN') //false
Number.isNaN(NaN) //true
```

## Değişken Türünü Değiştirmek (Type Coercion)

* Type Coercion; bir değişkenin türünü, başka bir değişkene dönüştürmeye yarayan yöntemdir.

---

## Template Literals Kullanımı

``` JavaScript
let ad= `Aycan`;
let soyad= `Yerdelen`;
//Eski kullanım
console.log("Benim adım "+ad+" "+ soyad);

//Yeni kullanım
console.log(`Benim adım ${ad} ${soyad}`);
```

``` javaScript
//Değişkenlerimizi tanımlayalım
const ad =`Aycan`
const soyad =`Yerdelen`
const gozRengi =`Kahverengi`
const yas =21

const kisi = "<p>"+ad+"</p>"+
              "<p>"+soyad+"</p>"+
              "<p>"+gozRengi+"</p>"+
              "<p>"+yas+"</p>"

document.body.innerHTML = kisi;

const kisi = `
<p>${ad}</>
<p>${soyad}</>
<p>${gozRengi}</>
<p>${yas}</>
`;

document.body.innerHTML = kisi;
```

---

## String Veri Türü İşlemleri

* Length Özelliği - Uzunluk Değerini Alma
* indexOf - Metin İçinde Arama Yapma
* lastIndexO f- Metin İçinde Arama Yapma
* Search - Metin İçinde Arama Yapma
* Slice - Metninden Parça Almak
* Replace – Metin Bulma ve Değiştirme
* toUpperCase metin içinde bulunan tüm karakterleri büyük harf yapmamıza olanak sağlar.
* toLowerCase metin içinde bulunan tüm karakterleri küçük harf yapmamıza olanak sağlar.
* Concat - Metin Birleştirme
* charAt- İndex Numarasına Göre Karakter Bulmak
* charCodeAt – İndex Numarasına Göre Karakterin Unicode Değerini Bulma
* Split – Metni Diziye Çevirme

---