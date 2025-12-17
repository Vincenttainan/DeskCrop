# DeskCrop  
---  
## [v0.0](https://github.com/Vincenttainan/DeskCrop/tree/e90e795b43aa4cfe0273bcc9bf0b837b3711f2e8)  

### 簡介  
DeskCrop 是一個小型懸浮視窗範例，永遠置於桌面最上方，目前僅包含 Mac 風格關閉按鈕  

### 功能  
* 懸浮視窗，始終在最上層  
* 自訂紅色圓形關閉按鈕  
    * 滑鼠移入顯示黑色叉叉  
    * 點擊關閉視窗

### 執行方式  
```bash
python DeskCrop.py
```

### 專案結構  
```
DeskCrop/
├── ui/
│   ├── Buttons.py       # Mac 風格關閉按鈕元件
│   └── __init__.py
├── DeskCrop.py          # 主程式
├── game/                # 後續遊戲邏輯
├── data/                # 後續存檔或設定
└── assets/              # 後續圖片、素材
```

### 未來規劃  
* 多塊土地的桌面種田遊戲  
* 自動收成 / 掛機功能  
* 作物品質系統與升級系統  
* UI 改進動畫效果  

---

## [v0.1](https://github.com/Vincenttainan/DeskCrop/tree/2c85b24bc3991132ddbf5271fe63d091e7d7e5b7)  

### 簡介  
新增一塊土地可種植與收穫，體驗基本掛機互動  

### 功能  
* v0.0 功能
* 單塊土地  
    * 空地 → 褐色  
    * 生長中 → 綠色  
    * 成熟 → 黃色  
* 滑鼠移過土地 → 種植/收成  

### 專案結構  
```
DeskCrop/
├── ui/
│   ├── tile_view.py     # 可視化的遊戲邏輯
│   ├── Buttons.py       # Mac 風格關閉按鈕元件
│   └── __init__.py
├── game/
│   └── tile.py          # 遊戲邏輯
├── DeskCrop.py          # 主程式
├── data/                # 後續存檔或設定
└── assets/              # 後續圖片、素材
```

### 未來規劃  
* 多塊土地管理    
* 自動收成 / 掛機功能  
* 作物品質系統與升級系統  
* UI 改進動畫效果  
