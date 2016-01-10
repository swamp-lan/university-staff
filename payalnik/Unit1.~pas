unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ComCtrls, Menus, StdCtrls;

type
  TForm1 = class(TForm)
    StatusBar1: TStatusBar;
    Edit1: TEdit;
    ScrollBar1: TScrollBar;
    Button1: TButton;
    MainMenu1: TMainMenu;
    dfg1: TMenuItem;
    Exit1: TMenuItem;
    About1: TMenuItem;
    Apply1: TMenuItem;
    Button2: TButton;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    ComboBox1: TComboBox;
    procedure ScrollBar1Change(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Exit1Click(Sender: TObject);
    procedure About1Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure ComboBox1Change(Sender: TObject);
    procedure Edit1Change(Sender: TObject);
    procedure Apply1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

uses Unit2;

{$R *.dfm}

procedure TForm1.ScrollBar1Change(Sender: TObject);
begin
    Form1.Edit1.Text :=  inttostr(Form1.ScrollBar1.Position);
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
Application.Terminate;
end;

procedure TForm1.Exit1Click(Sender: TObject);
begin
Application.Terminate;
end;

procedure TForm1.About1Click(Sender: TObject);
begin
Form2.show();
end;

procedure TForm1.Button1Click(Sender: TObject);
var
 x:integer;
begin

  with Application do
  begin
//    NormalizeTopMosts;
    MessageBox('Illegal function call dsHddAccess()', 'Error', 18);
    Application.Terminate;

  //  RestoreTopMosts;
  end;



end;

procedure TForm1.ComboBox1Change(Sender: TObject);
begin
  with Application do
  begin
//    NormalizeTopMosts;
    MessageBox('Wrong HDD model selected', 'Error', 16);


  //  RestoreTopMosts;
  end;
end;

procedure TForm1.Edit1Change(Sender: TObject);
begin

Form1.ScrollBar1.Position :=  strtoint(Form1.Edit1.Text);
end;

procedure TForm1.Apply1Click(Sender: TObject);
begin
with Application do
  begin
//    NormalizeTopMosts;
    MessageBox('Illegal function call dsHddAccess()', 'Error', 18);
    Application.Terminate;

  //  RestoreTopMosts;
  end;
end;

end.
